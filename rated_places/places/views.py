from django.shortcuts import render

import requests

from key import getkey



def index(request):
    return render(request,'index.html') 

def category(request):
    city_name = request.GET["city"]
    category = {'Bars' : "Bars.PNG","Museuem" : "museum.png","Hospitals" : "hospitals.PNG","Gym" : "gym.png", "Hotels" : "hotels.png","Parks" : "parks.png","Jwellery" : "jwells.png","Zoo" : "zoo.png"}

    return render(request,"category.html",{"name" : city_name,"category" : category})

def places(request):
    name = request.GET['name']
    categories = {'Bars' : "bar","Museuem" : "museum","Hospitals" : "hospital","Gym" : "gym", "Hotels" : "restaurant","Parks" : "park","Jwellery" : "jewelry_store" ,"Zoo" : "zoo"}
    category = request.GET['category']
    
    req = requests.get('https://maps.googleapis.com/maps/api/geocode/json?components=country:IN%7Clocality:'+ name + '&key=' + getkey())
    req = req.json()
    lat =  req['results'][0]['geometry']['location']['lat']
    lang =  req['results'][0]['geometry']['location']['lng']

    r1 = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+ str(lat) + ',' + str(lang) + '&radius=150000&type='+ categories[category] + '&key='+getkey())

    r1 = r1.json()
    d = {}
    for i in r1['results']:
        
        if 'rating' in i:
            d[i['name']] = [i['rating'],i['user_ratings_total']]
        else:
            d[i['name']] = ["",0]

    print(d)
    return render(request,"places.html",{"name" : name,"categories" : categories,"category" : category,"places" : d})
