from django.contrib import admin
from .models import Hiretuber
# Register your models here.

class HiretuberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'tuber_name' )
    list_display_links = ('first_name', 'last_name' ,'tuber_name')
    search_fields = ('first_name', 'last_name', 'tuber_name')
    list_filter = ('first_name', 'last_name', 'tuber_name')

admin.site.register(Hiretuber, HiretuberAdmin)