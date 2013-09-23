from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from .models import Ticket, Company, Tier, Status
from .forms import EditTicketForm, CommentForm, NewTicketForm


class TicketChange:
    def __init__(self, field_name=None, old_value=None, new_value=None, date_time=None, changed_by=None):
        self.field_name = field_name
        self.old_value = old_value
        self.new_value = new_value
        self.date_time = date_time
        self.changed_by = changed_by


def index(request):
    return render(
        request,
        'tickets/index.html',
        {}
    )


@login_required
def open(request):
    tickets = Ticket.objects.filter(status__name="Open")

    return render(
        request,
        'tickets/open.html',
        {'tickets': tickets}
    )


@login_required
def comment(request, ticket_id):
    ticket_model = Ticket.objects.get(pk=ticket_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, {})
        if form.is_valid():
            comment = form.save(commit=False)
            comment.date_time = datetime.now()
            comment.ticket = ticket_model
            comment.user = request.user
            comment.save()

    return redirect('ticket', ticket_id=ticket_id)


@login_required
def ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
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
            'events': events
        }
    )


@login_required
def tier(request, tier_id):
    tickets = Ticket.objects.filter(tier_id=tier_id)
    tier = Tier.objects.get(pk=tier_id)

    return render(
        request,
        'tickets/tier.html',
        {
            'tickets': tickets,
            'tier': tier
        }
    )


@login_required
def company(request, company_id):
    company = Company.objects.get(pk=company_id)

    return render(
        request,
        'tickets/company.html',
        {'company': company}
    )


@login_required
def new_ticket(request):
    if request.method == 'POST':
        form = NewTicketForm(request.POST, {})
        if(form.is_valid()):
            ticket = form.save(commit=False)
            ticket.changed_by = request.user
            ticket.save()
            return HttpResponseRedirect('/tickets/')
    else:
        form = NewTicketForm()

    return render(
        request,
        'tickets/new_ticket.html',
        {'form': form}
    )
