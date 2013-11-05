from django.contrib import admin
from .models import Company, Status, Ticket, Tier, TicketComment, Department, TicketTierChange, TicketStatusChange, Product, ProductVersion


admin.site.register(Company)
admin.site.register(Status)
admin.site.register(Ticket)
admin.site.register(Tier)
admin.site.register(TicketComment)
admin.site.register(TicketTierChange)
admin.site.register(TicketStatusChange)
admin.site.register(Department)
admin.site.register(Product)
admin.site.register(ProductVersion)
