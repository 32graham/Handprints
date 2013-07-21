from django.shortcuts import render
from .models import Ticket


def index(request):
    tickets = Ticket.objects.all()

    return render(
        request,
        'tickets/index.html',
        {'tickets': tickets}
    )
