from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView
from datetime import datetime
from django.utils.timezone import utc
from .models import Ticket, TicketStatusChange, TicketTierChange
from .forms import EditTicketForm, CommentForm, NewTicketForm


class IndexView(TemplateView):
    template_name = 'index.html'


class TicketList(ListView):
    model = Ticket
    context_object_name = 'tickets'
    paginate_by = 15

    def get_queryset(self):
        queryset = Ticket.objects.all()
        if 'tier_id' in self.kwargs:
            queryset = queryset.filter(tier__pk=self.kwargs['tier_id'])
        if 'status_id' in self.kwargs:
            queryset = queryset.filter(status__pk=self.kwargs['status_id'])
        if 'company_id' in self.kwargs:
            queryset = queryset.filter(company__pk=self.kwargs['company_id'])
        if 'department_id' in self.kwargs:
            queryset = queryset.filter(tier__department__pk=self.kwargs['department_id'])
        return queryset

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TicketList, self).dispatch(*args, **kwargs)


def get_events(ticket):
    comments = list(ticket.comments.all())
    tier_changes = list(ticket.tier_changes.all())
    status_changes = list(ticket.status_changes.all())

    events = comments + tier_changes + status_changes
    events = sorted(events, key=lambda event: event.date_time)

    return events


@login_required
def ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    events = get_events(ticket)

    if request.method == 'POST' and 'ticket_post' in request.POST:
        ticketForm = EditTicketForm(request.POST, instance=ticket)
        commentForm = CommentForm()
        if ticketForm.is_valid():
            return handle_ticket_post(request, ticketForm)
    elif request.method == 'POST' and 'comment_post' in request.POST:
        commentForm = CommentForm(request.POST, request.FILES)
        ticketForm = EditTicketForm(instance=ticket)
        if commentForm.is_valid():
            return handle_comment_post(request, commentForm, ticket)
    else:
        ticketForm = EditTicketForm(instance=ticket)
        commentForm = CommentForm()

    return render(
        request,
        'tickets/ticket.html',
        {
            'ticket': ticket,
            'ticket_form': ticketForm,
            'comment_form': commentForm,
            'events': events,
        }
    )


def handle_ticket_post(request, ticketForm):
    model = ticketForm.save(commit=False)
    previous_ticket = Ticket.objects.get(pk=model.pk)
    model.save()

    if previous_ticket is None or previous_ticket.status != model.status:
        statusChange = TicketStatusChange()
        statusChange.ticket = model
        statusChange.date_time = datetime.utcnow().replace(tzinfo=utc)
        statusChange.new_status = model.status
        statusChange.user = request.user
        statusChange.save()

    if previous_ticket is None or previous_ticket.tier != model.tier:
        tierChange = TicketTierChange()
        tierChange.ticket = model
        tierChange.date_time = datetime.utcnow().replace(tzinfo=utc)
        tierChange.new_tier = model.tier
        tierChange.user = request.user
        tierChange.save()

    return HttpResponseRedirect('/tickets/' + str(model.pk) + '/')


def handle_comment_post(request, commentForm, ticket):
    comment = commentForm.save(commit=False)
    comment.date_time = datetime.now()
    comment.ticket = ticket
    comment.user = request.user
    comment.save()
    return HttpResponseRedirect('/tickets/' + str(ticket.pk) + '/')


@login_required
def new_ticket(request):
    if request.method == 'POST':
        form = NewTicketForm(request.POST, {})
        if(form.is_valid()):
            ticket = form.save(commit=False)
            ticket.created_date_time = datetime.utcnow().replace(tzinfo=utc)
            ticket.user_created = request.user
            ticket.save()
            return HttpResponseRedirect('/tickets/status/1/')
    else:
        form = NewTicketForm()

    return render(
        request,
        'tickets/new_ticket.html',
        {'form': form}
    )
