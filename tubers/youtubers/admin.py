from django.contrib import admin
from .models import *
from django.utils.html import format_html

class Ytadmin(admin.ModelAdmin):
    def ytphoto(self,object):
        return format_html('<img src= "{}" width="120" />'.format(object.photo.url))
    list_display = ('id','ytphoto','first_name','subs','is_featured')
    search_fields = ('first_name','camera')
    list_filter = ('city','category')
    list_display_links = ('id','first_name','subs')
    list_editable = ('is_featured',)




admin.site.register(Youtuber,Ytadmin)
# Register your models here.
