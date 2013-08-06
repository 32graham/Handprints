from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import Ticket
from .forms import CommentForm


def index(request):
    tickets = Ticket.objects.all()

    return render(
        request,
        'tickets/index.html',
        {'tickets': tickets}
    )


def ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, {})
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket_id = ticket_id
            comment.date_time = datetime.now()
            comment.save()

            return HttpResponseRedirect('/tickets/')
    else:
        form = CommentForm(initial={'ticket_id': ticket_id, 'date_time': datetime.now()})

    return render(
        request,
        'tickets/ticket.html',
        {
            'ticket': ticket,
            'comment_form': form
        }
    )


def tier(request, tier_id):
    tickets = Ticket.objects.filter(tier_id=tier_id)

    return render(
        request,
        'tickets/tier.html',
        {'tickets': tickets}
    )
