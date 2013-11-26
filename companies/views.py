from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import CompanyForm


@login_required
def company_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    open_tickets = company.ticket_set.filter(status__name='Open')

    recently_closed_tickets = company.ticket_set.filter(
            status__name='Closed'
        ).filter(
            status_changes__new_status__name='Closed'
        ).order_by(
            '-status_changes__date_time'
        )[:5]

    if request.method == 'POST':
        form = CompanyForm(request.POST, {})
        if form.is_valid():
            form.save()
    else:
        form = CompanyForm()

    return render(
        request,
        'tickets/company_detail.html',
        {
            'company': company,
            'open_tickets': open_tickets,
            'recently_closed_tickets': recently_closed_tickets,
            'form': form,
        }
    )
