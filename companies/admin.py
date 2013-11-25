from django.contrib import admin
from .models import Company, Product, ProductVersion


admin.site.register(Company)
admin.site.register(Product)
admin.site.register(ProductVersion)
