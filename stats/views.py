from django.shortcuts import render
from tickets.models import Company, Tier
from django.db.models import Count


def overall(request):
    companies = Company.objects.annotate(num_tickets=Count('ticket'))
    tiers = Tier.objects.annotate(num_tickets=Count('ticket'))

    company_vs_ticket_count = {}
    for company in companies:
        company_vs_ticket_count[str(company.name)] = company.num_tickets

    tier_vs_ticket_count = {}
    for tier in tiers:
        tier_vs_ticket_count[str(tier.name)] = tier.num_tickets

    return render(
        request,
        'stats/overall_stats.html',
        {
            'company_vs_ticket_count': company_vs_ticket_count,
            'tier_vs_ticket_count': tier_vs_ticket_count,
        }
    )
