from django.contrib import admin

from .models import Services, Slider, Team, About

from django.utils.html import format_html

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src= "{}" width= "49" />'.format(object.photo.url))
    list_display = ('headline', 'myphoto')
    list_display_link = ('headline', 'myphoto')
    list_filter = ('headline',)
    search_fields = ('headline',)
    
class SliderAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src= "{}" width= "49" />'.format(object.photo.url))
    list_display = ('headline', 'myphoto', 'button_text')
    list_display_links = ('headline', 'myphoto', 'button_text')
    list_filter = ('headline', 'button_text')
    search_fields = ('headline', 'button_text')
    
class TeamAdmin(admin.ModelAdmin):
    
    def myphoto(self, object):
        return format_html('<img src= "{}" width= "49" />'.format(object.photo.url))
    
    list_display = ('id', 'myphoto', 'first_name', 'role', 'created_date')
    list_display_links =  ('first_name', 'id', 'role')
    search_fields = ('first_name', 'role')
    list_filter = ('role',)

class ServiceAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src= "{}" width= "49" />'.format(object.photo.url))
    list_display = ('headline', 'myphoto', 'created_date')
    list_display_links = ('headline', )
    search_fields = ('headline',)
    list_filter = ('headline',)

admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Services, ServiceAdmin)
admin.site.register(About, AboutAdmin)