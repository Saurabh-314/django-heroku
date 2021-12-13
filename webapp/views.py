from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Registration
import requests
from django.core.files.storage import FileSystemStorage


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        brand = request.POST["brand"]
        typ = request.POST["typ"]
        desc = request.POST["desc"]
        img = request.FILES["img"]
        
        data = Registration(name=name,price=price,typ=typ,brand=brand,desc=desc,img=img)
        data.save()

    return render(request,'index.html')

def details(request):
    all_data = Registration.objects.all()
    return render(request,'details.html',{"details":all_data})

def info(request,myid):
    dt = Registration.objects.filter(id=myid)
    return render(request,'info.html',{'id1':dt})
