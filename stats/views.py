from django.shortcuts import render
from tickets.models import Company, Tier, Ticket
from django.db.models import Count
from datetime import datetime, timedelta
from itertools import groupby
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_staff)
def overall(request):
    return render(
        request,
        'stats/overall_stats.html',
        {
            'company_vs_ticket_count': get_company_vs_ticket_count(),
            'tier_vs_ticket_count': get_tier_vs_ticket_count(),
            'count_vs_day': get_creations_by_day(),
        }
    )


def get_company_vs_ticket_count():
    companies = Company.objects.annotate(num_tickets=Count('ticket')).order_by('-num_tickets')[:5]

    company_vs_ticket_count = {}
    for company in companies:
        company_vs_ticket_count[str(company.name)] = company.num_tickets

    return company_vs_ticket_count


def get_tier_vs_ticket_count():
    tiers = Tier.objects \
        .filter(ticket__status__name='Open') \
        .annotate(num_tickets=Count('ticket'))

    tier_vs_ticket_count = {}
    for tier in tiers:
        tier_vs_ticket_count[str(tier.name)] = tier.num_tickets

    return tier_vs_ticket_count


def get_creations_by_day():
    items1 = Ticket.objects \
        .filter(
            created_date_time__lte=datetime.today(),
            created_date_time__gt=datetime.today()- timedelta(days=30)
        )

    time_vs_created_count = {}
    for time, tickets in groupby(items1, lambda x: x.created_date_time.date()):
        for ticket in tickets:
            if str(time) in time_vs_created_count:
                time_vs_created_count[str(time)] += 1
            else:
                time_vs_created_count[str(time)] = 1

    return time_vs_created_count
