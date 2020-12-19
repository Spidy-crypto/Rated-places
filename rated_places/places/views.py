from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request,'index.html') 

def category(request):
    city_name = request.GET["city"]
    return render(request,"category.html",{"name" : city_name})