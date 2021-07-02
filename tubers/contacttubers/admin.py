from django.contrib import admin
from django.db import models
from .models import Contacttuber

class Ctuber(admin.ModelAdmin):
    list_display=('full_name','email','phone')
    list_display_links=('full_name','email','phone')



admin.site.register(Contacttuber,Ctuber)

# Register your models here.
