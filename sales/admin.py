from django.contrib import admin
from .models import Sale, SaleItem


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    pass
