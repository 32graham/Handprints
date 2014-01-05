from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied
from datetime import datetime
from django.utils.timezone import utc
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Ticket, TicketAssigneeChangeSet, TicketAssigneeAdded, TicketAssigneeRemoved, Tier, Status
from .forms import EditTicketForm, StaffCommentForm, StandardCommentForm, StandardNewTicketForm, StaffNewTicketForm
from .filters import TicketFilter


class IndexView(TemplateView):
    template_name = 'index.html'


def get_events(request, ticket):

    if(request.user.is_staff):
        comments = list(ticket.comments.all())
        assignee_changes = list(ticket.assignee_changes.all())
    else:
        comments = list(ticket.comments.filter(is_public=True))
        assignee_changes = []

    tier_changes = list(ticket.tier_changes.all())
    status_changes = list(ticket.status_changes.all())

    events = comments + tier_changes + status_changes + assignee_changes
    events = sorted(events, key=lambda event: event.date_time)

    return events


@login_required
def ticket(request, ticket_id):
    if(request.user.is_staff):
        return staff_ticket(request, ticket_id)
    else:
        return standard_ticket(request, ticket_id)


@login_required
def standard_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)

    if not ticket.company.pk == request.user.profile.company.pk:
        raise PermissionDenied

    events = get_events(request, ticket)

    if request.method == 'POST':
        ticket.profile_changed = request.user.profile
        commentForm = StandardCommentForm(request.POST, request.FILES)
        if commentForm.is_valid():
            return handle_comment_post(request, commentForm, ticket)
    else:
        commentForm = StandardCommentForm()

    return render(
        request,
        'tickets/ticket.html',
        {
            'ticket': ticket,
            'comment_form': commentForm,
            'events': events,
        }
    )


@login_required
def staff_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    events = get_events(request, ticket)

    if request.method == 'POST' and 'ticket_post' in request.POST:
        ticket.profile_changed = request.user.profile
        ticketForm = EditTicketForm(request.POST, instance=ticket)
        commentForm = StaffCommentForm()
        if ticketForm.is_valid():
            return handle_ticket_post(ticketForm)
    elif request.method == 'POST' and 'comment_post' in request.POST:
        ticket.profile_changed = request.user.profile
        commentForm = StaffCommentForm(request.POST, request.FILES)
        ticketForm = EditTicketForm(instance=ticket)
        if commentForm.is_valid():
            return handle_comment_post(request, commentForm, ticket)
    else:
        ticketForm = EditTicketForm(instance=ticket)
        commentForm = StaffCommentForm()

    return render(
        request,
        'tickets/staff_ticket.html',
        {
            'ticket': ticket,
            'ticket_form': ticketForm,
            'comment_form': commentForm,
            'events': events,
        }
    )


def handle_ticket_post(ticketForm):
    old_model = ticketForm.instance
    old_assignees = set(old_model.assignees.all())

    model = ticketForm.save()

    new_assignees = set(model.assignees.all())
    added = new_assignees - old_assignees
    removed = old_assignees - new_assignees

    if len(added) + len(removed) > 0:
        date_time = datetime.utcnow().replace(tzinfo=utc)

        change_set = TicketAssigneeChangeSet.objects.create(
            ticket=model,
            date_time=date_time,
            profile=model.profile_changed)

        for added in added:
            TicketAssigneeAdded.objects.create(change_set=change_set, assignee=added)

        for removed in removed:
            TicketAssigneeRemoved.objects.create(change_set=change_set, assignee=removed)

    return HttpResponseRedirect(reverse('ticket', args=(str(model.pk),)))


@login_required
def handle_comment_post(request, commentForm, ticket):
    comment = commentForm.save(commit=False)
    comment.date_time = datetime.now()
    comment.ticket = ticket
    comment.profile = request.user.profile

    if not request.user.is_staff:
        comment.is_public = True

    comment.save()
    return HttpResponseRedirect(reverse('ticket', args=(str(ticket.pk),)))


@login_required
def new_ticket(request):
    if request.user.is_staff:
        return staff_new_ticket(request)
    else:
        return standard_new_ticket(request)


@login_required
def staff_new_ticket(request):
    if request.method == 'POST':
        form = StaffNewTicketForm(request.POST, {})

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_date_time = datetime.utcnow().replace(tzinfo=utc)
            ticket.profile_created = request.user.profile
            ticket.profile_changed = request.user.profile
            ticket.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('tickets'))
    else:
        form = StaffNewTicketForm(initial={
            'status': 1,
            'tier': 1,
            'product': 1,
        })

    return render(
        request,
        'tickets/new_ticket.html',
        {'form': form}
    )


@login_required
def standard_new_ticket(request):
    if request.method == 'POST':
        form = StandardNewTicketForm(request.POST, {})

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_date_time = datetime.utcnow().replace(tzinfo=utc)
            ticket.profile_created = request.user.profile
            ticket.profile_changed = request.user.profile
            ticket.company = request.user.profile.company
            ticket.tier = Tier.objects.get(name='Tier 1')
            ticket.status = Status.objects.get(name='Open')
            ticket.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('company', args=(str(request.user.profile.company.pk),)))
    else:
        form = StandardNewTicketForm(initial={
            'product': 1,
        })

    return render(
        request,
        'tickets/new_ticket.html',
        {'form': form}
    )


@login_required
def ticket_list(request):
    if not request.user.is_staff:
        raise PermissionDenied

    f = TicketFilter(request.GET, queryset=Ticket.objects.all())
    paginator = Paginator(f.qs, 50)

    page = request.GET.get('page')
    try:
        obj_list = paginator.page(page)
    except PageNotAnInteger:
        obj_list = paginator.page(1)
    except EmptyPage:
        obj_list = paginator.page(paginator.num_pages)

    return render(
        request,
        'tickets/filtered_ticket_list.html',
        {
            'filter': f,
            'object_list': obj_list,
            'request': request
        }
    )
