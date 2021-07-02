from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Youtuber

def youtubers(request):
    tubers = Youtuber.objects.all()
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()
    camera_search =Youtuber.objects.values_list('camera',flat=True).distinct()
    category_search = Youtuber.objects.values_list('category',flat=True).distinct()
    if 'keyword' in  request.GET:
        keyword =request.GET['keyword']
        if keyword:
            tubers = tubers.filter(Description__icontains = keyword)

    if 'city' in request.GET:
        city= request.GET['city']
        if city :
            tubers = tubers.filter(city__iexact=city)
    
    if 'camera' in request.GET:
        camera= request.GET['camera']
        if camera :
            tubers = tubers.filter(camera__iexact = camera) 
    if 'category' in request.GET:
        category= request.GET['category']
        if category :
            tubers = tubers.filter(category__iexact = category)        
    
    
    data={

        'tubers':tubers,
        'city_search': city_search,
        'camera_search': camera_search,
        'category_search': category_search,
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtuber_detail(request,id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data={

        'tuber':tuber,
    }
    return render(request, 'youtubers/youtuber_detail.html',data)

def search(request):
    tubers = Youtuber.objects.all()
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()
    camera_search =Youtuber.objects.values_list('camera',flat=True).distinct()
    category_search = Youtuber.objects.values_list('category',flat=True).distinct()
    if 'keyword' in  request.GET:
        keyword =request.GET['keyword']
        if keyword:
            tubers = tubers.filter(Description__icontains = keyword)

    if 'city' in request.GET:
        city= request.GET['city']
        if city :
            tubers = tubers.filter(city__iexact=city)
    
    if 'camera' in request.GET:
        camera= request.GET['camera']
        if camera :
            tubers = tubers.filter(camera__iexact = camera) 
    if 'category' in request.GET:
        category= request.GET['category']
        if category :
            tubers = tubers.filter(category__iexact = category)        
    
    
    data={

        'tubers':tubers,
        'city_search': city_search,
        'camera_search': camera_search,
        'category_search': category_search,
    }
    return render(request, 'youtubers/search.html',data)


