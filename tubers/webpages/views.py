from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from youtubers.models import Youtuber

def home(request):
    sliders=Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured= True)
    onboard_youtubers = Youtuber.objects.order_by('-created_date')
    data={
        'sliders':sliders,
        'teams':teams,
        'featured_youtubers':featured_youtubers,
        'onboard_youtubers':onboard_youtubers,
    }
    return  render(request,'webpages/home.html',data)

def about(request):
    teams = Team.objects.all()
    about_info= About.objects.all()
    data = {
        'teams':teams,
        'about_info':about_info
    }
    return render(request,'webpages/about.html',data)

def contact(request):
    return render(request,'webpages/contact.html')

def services(request):
    teams = Team.objects.all()
    data={
        'teams':teams,
    }
    return render(request,'webpages/services.html',data)

