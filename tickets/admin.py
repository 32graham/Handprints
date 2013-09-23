from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Company, Status, Ticket, Tier, TicketComment


admin.site.register(Company)
admin.site.register(Status)
admin.site.register(Ticket, SimpleHistoryAdmin)
admin.site.register(Tier)
admin.site.register(TicketComment)
