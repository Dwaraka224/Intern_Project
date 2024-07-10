from django.shortcuts import render
from datetime import datetime
from Python_Web_App.forms import *
from django.http import HttpResponse
# Create your views here.


def home(request):
    current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    UFO=UserForm()
    if request.method =='POST':
        UFDO=UserForm(request.POST)
        if UFDO.is_valid():
            UFDO.save()
            User_Details=User_Info.objects.all()
            return render(request,'Display_user_details.html',{'User_Details':User_Details})
    
    return render(request,'home.html',{'time':current_time,'UFO':UFO})




# def Display_user_details(request):
    

    