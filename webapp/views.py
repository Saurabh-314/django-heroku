from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Registration


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        brand = request.POST["brand"]
        typ = request.POST["typ"]
        desc = request.POST["desc"]
        img = request.POST["img"]
        
        data = Registration(name=name,price=price,typ=typ,brand=brand,desc=desc,img=img)
        data.save()

    return render(request,'index.html')

def details(request):
    all_data = Registration.objects.all()
    return render(request,'details.html',{"details":all_data})

def info(request,myid):
    # print(request.GET)
    dt = Registration.objects.filter(id=myid)
    # print(dt)
    return render(request,'info.html',{'id1':dt})
    # return render(request,'info.html')


# def info(request,myid):
    # fetch the product using the id
    # product = Registration.objects.filter(id=myid)
    # return render(request, 'info.html',{'product':product[0]})