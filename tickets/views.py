from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import Ticket, Company
from .forms import TicketForm, CommentForm


def index(request):
    tickets = Ticket.objects.all()

    return render(
        request,
        'tickets/index.html',
        {'tickets': tickets}
    )


def comment(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, {})
        if form.is_valid():
            comment = form.save(commit=False)
            comment.date_time = datetime.now()
            comment.ticket = ticket
            comment.save()

    return index(request)


def ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)

    if request.method == 'POST':
        ticketForm = TicketForm(request.POST, {})
        if ticketForm.is_valid():
            formTicket = ticketForm.save(commit=False)
            ticket.tier = formTicket.tier
            ticket.save()
            return HttpResponseRedirect('/tickets/' + ticket_id + '/')
    else:
        ticketForm = TicketForm(instance=ticket)

    commentForm = CommentForm()

    return render(
        request,
        'tickets/ticket.html',
        {
            'ticket': ticket,
            'ticket_form': ticketForm,
            'comment_form': commentForm
        }
    )


def tier(request, tier_id):
    tickets = Ticket.objects.filter(tier_id=tier_id)

    return render(
        request,
        'tickets/tier.html',
        {'tickets': tickets}
    )


def company(request, company_id):
    company = Company.objects.get(pk=company_id)

    return render(
        request,
        'tickets/company.html',
        {'company': company}
    )
