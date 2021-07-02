from django.contrib import admin
from .models import *
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src= "{}" width="120" />'.format(object.photo.url))


    list_display=('id','myphoto', 'first_name', 'role', 'created_date')
    list_display_links=('id', 'first_name', 'role')
    search_fields = ('first_name', 'role',)
class Slide(admin.ModelAdmin):
    def sphoto(self,object):
        return format_html('<img src= "{}" width="180: /> '.format(object.photo.url))
    list_display=('headline','sphoto','button_text')
    list_display_links=('headline','button_text',)

admin.site.register(Slider,Slide)
admin.site.register(Team, TeamAdmin)
admin.site.register(About)

# Register your models here.
