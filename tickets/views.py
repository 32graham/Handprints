from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from datetime import datetime
from .models import Ticket, Tier, Status
from .forms import EditTicketForm, CommentForm, NewTicketForm


class TicketChange:
    def __init__(self, field_name=None, old_value=None, new_value=None, date_time=None, changed_by=None):
        self.field_name = field_name
        self.old_value = old_value
        self.new_value = new_value
        self.date_time = date_time
        self.changed_by = changed_by


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
        return queryset

@login_required
def comment(request, ticket_id):
    ticket_model = get_object_or_404(Ticket, pk=ticket_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.date_time = datetime.now()
            comment.ticket = ticket_model
            comment.user = request.user
            comment.save()

    return redirect('ticket', ticket_id=ticket_id)


@login_required
def ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    events = list(ticket.ticketcomment_set.all())

    all_changes = ticket.history.order_by('history_date')

    previous_change = None
    for change in all_changes:
        if previous_change != None:
            if change.tier_id != previous_change.tier_id:
                new_tier = Tier.objects.get(pk=change.tier_id)
                old_tier = Tier.objects.get(pk=previous_change.tier_id)
                changed_by = User.objects.get(pk=change.changed_by_id)
                events.append(TicketChange('Tier', old_tier.name, new_tier.name, change.history_date, changed_by.get_full_name()))

            if change.status_id != previous_change.status_id:
                new_status = Status.objects.get(pk=change.status_id)
                old_status = Status.objects.get(pk=previous_change.status_id)
                changed_by = User.objects.get(pk=change.changed_by_id)
                events.append(TicketChange('Status', old_status.name, new_status.name, change.history_date, changed_by.get_full_name()))

            if change.assignee_id != previous_change.assignee_id:
                new_assignee = User.objects.get(pk=change.assignee_id)
                old_assignee = User.objects.get(pk=previous_change.assignee_id)
                changed_by = User.objects.get(pk=change.changed_by_id)
                events.append(TicketChange('Assignee', old_assignee.get_full_name(), new_assignee.get_full_name(), change.history_date, changed_by.get_full_name()))

        previous_change = change

    events = sorted(events, key=lambda event: event.date_time)

    if request.method == 'POST':
        ticketForm = EditTicketForm(request.POST, instance=ticket)
        if ticketForm.is_valid():
            model = ticketForm.save(commit=False)
            model.changed_by = request.user
            model.save()
            return HttpResponseRedirect('/tickets/' + ticket_id + '/')
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


@login_required
def new_ticket(request):
    if request.method == 'POST':
        form = NewTicketForm(request.POST, {})
        if(form.is_valid()):
            ticket = form.save(commit=False)
            ticket.changed_by = request.user
            ticket.save()
            return HttpResponseRedirect('/tickets/status/1/')
    else:
        form = NewTicketForm()

    return render(
        request,
        'tickets/new_ticket.html',
        {'form': form}
    )
