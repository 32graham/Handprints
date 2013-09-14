from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import Ticket, Company, Tier
from .forms import EditTicketForm, CommentForm, NewTicketForm


def index(request):
    tickets = Ticket.objects.all()

    return render(
        request,
        'tickets/index.html',
        {'tickets': tickets}
    )


def comment(request, ticket_id):
    ticket_model = Ticket.objects.get(pk=ticket_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, {})
        if form.is_valid():
            comment = form.save(commit=False)
            comment.date_time = datetime.now()
            comment.ticket = ticket_model
            comment.save()

    return redirect('ticket', ticket_id=1)


def ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)

    if request.method == 'POST':
        ticketForm = EditTicketForm(request.POST, {})
        if ticketForm.is_valid():
            formTicket = ticketForm.save(commit=False)
            ticket.tier = formTicket.tier
            ticket.save()
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
            'comment_form': commentForm
        }
    )


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


def company(request, company_id):
    company = Company.objects.get(pk=company_id)

    return render(
        request,
        'tickets/company.html',
        {'company': company}
    )

def new_ticket(request):
    if request.method == 'POST':
        form = NewTicketForm(request.POST, {})
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/tickets/')
    else:
        form = NewTicketForm()

    return render(
        request,
        'tickets/new_ticket.html',
        {'form': form}
    )
