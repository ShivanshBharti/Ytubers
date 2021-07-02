from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Contacttuber

# Create your views here.
def contacttuber(request):
    if request.method == 'POST':
        full_name=request.POST['full_name']
        email=request.POST['email']
        phone=request.POST['phone']
        company=request.POST['company']
        subject=request.POST['subject']
        message=request.POST['message']
        #user_id = request.POST['user_id']
    
        contacttuber = Contacttuber(full_name=full_name,email=email,phone=phone,company=company,subject=subject,message=message)
        contacttuber.save()
        messages.success(request,"Thanks for reaching us!")
        return redirect('contact')
