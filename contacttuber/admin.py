from django.contrib import admin
from .models import Contacttuber
# Register your models here.

class ContacttuberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'company_name' )
    list_display_links = ('full_name', )
    search_fields = ('full_name', 'company_name')
    list_filter = ('full_name', 'company_name')

admin.site.register(Contacttuber, ContacttuberAdmin)