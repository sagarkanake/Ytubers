from django.contrib import admin
from .models import ContactInfo
# Register your models here.

class CAdmin(admin.ModelAdmin):
    list_display = ('email', 'contact')
    list_display_links = ('email', 'contact')
    list_filter = ('email', 'contact')
    search_fields = ('email', 'contact')


admin.site.register(ContactInfo, CAdmin)