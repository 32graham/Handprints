from django.contrib import admin
from .models import Company, TicketState, Ticket, Tier


admin.site.register(Company)
admin.site.register(TicketState)
admin.site.register(Ticket)
admin.site.register(Tier)
