from django.contrib import admin
from .models import Employ, Job

# Register your models here.
class EmployAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'job',)
    search_fields = ('name',)

class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)

admin.site.register(Employ, EmployAdmin)
admin.site.register(Job, JobAdmin)