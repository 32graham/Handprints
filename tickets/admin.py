from django.contrib import admin
from .models import Status, Ticket, Tier, TicketComment, Department, TicketTierChange, TicketStatusChange


admin.site.register(Status)
admin.site.register(Ticket)
admin.site.register(Tier)
admin.site.register(TicketComment)
admin.site.register(TicketTierChange)
admin.site.register(TicketStatusChange)
admin.site.register(Department)
