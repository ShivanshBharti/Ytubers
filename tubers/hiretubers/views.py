from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Hiretuber
from django.contrib import messages

# Create your views here.
def hiretuber(request):
    if request.method == 'POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        tuber_id =request.POST['tuber_id']
        city =request.POST['city']
        phone =request.POST['phone']
        state =request.POST['state']
        email =request.POST['email']
        message =request.POST['message']
        user_id =request.POST['user_id']
        

        hiretuber = Hiretuber(first_name=first_name,last_name=last_name,tuber_id=tuber_id,city=city,phone=phone,state=state,email=email,message=message,user_id=user_id)
        hiretuber.save()
        messages.success(request,'Thanks for reaching out!')
        return redirect('home')