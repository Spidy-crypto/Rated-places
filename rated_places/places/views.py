from django.shortcuts import render
# Create your views here.

import requests


def index(request):
    return render(request,'index.html') 

def category(request):
    city_name = request.GET["city"]
    category = {'Bars' : "Bars.PNG","Beaches" : "beaches.png","Hospitals" : "hospitals.PNG","Hostels" : "hostels.png", "Hotels" : "hotels.png","Parks" : "parks.png"}

    return render(request,"category.html",{"name" : city_name,"category" : category})

def places(request):
    name = request.GET['name']
    categories = {'Bars' : "bar","Beaches" : "beaches.png","Hospitals" : "hospital","Hostels" : "hostels.png", "Hotels" : "hotels.png","Parks" : "park"}
    category = request.GET['category']

    req = requests.get('https://maps.googleapis.com/maps/api/geocode/json?components=country:IN%7Clocality:'+ name + '&key=AIzaSyBD_k7MQjrFHJPUT9MupbUKWOHOsCwl23o')
    req = req.json()
    lat =  req['results'][0]['geometry']['location']['lat']
    lang =  req['results'][0]['geometry']['location']['lng']

    r1 = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+ str(lat) + ',' + str(lang) + '&radius=150000&type='+ 'park' + '&key=AIzaSyBD_k7MQjrFHJPUT9MupbUKWOHOsCwl23o')

    r1 = r1.json()
    d = {}
    for i in r1['results']:
        
        if 'rating' in i:
            d[i['name']] = [i['rating'],i['user_ratings_total']]
        else:
            d[i['name']] = ["",0]

    return render(request,"places.html",{"name" : name,"categories" : categories,"category" : category,"places" : d})