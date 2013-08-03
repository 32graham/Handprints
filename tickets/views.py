from django.shortcuts import render
from .models import Ticket


def index(request):
    tickets = Ticket.objects.all()

    return render(
        request,
        'tickets/index.html',
        {'tickets': tickets}
    )


def ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)

    return render(
        request,
        'tickets/ticket.html',
        {'ticket': ticket}
    )
