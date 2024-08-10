from django.contrib import admin
from .models import Invoice

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('name', "value", 'is_pay',)
    search_fields = ('name',)

admin.site.register(Invoice, InvoiceAdmin)