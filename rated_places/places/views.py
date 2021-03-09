from django.shortcuts import render,redirect
import requests
from key import getkey
import shutil, os
from pathlib import Path
from django.conf import settings as django_settings
from places.models import addToFav

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
            d[i['name']] = [i['rating'],i['user_ratings_total'],i['place_id']]
        else:
            d[i['name']] = ["",0,i['place_id']]

    return render(request,"places.html",{"name" : name,"categories" : categories,"category" : category,"places" : d})

def place_detail(request):

    city_name = request.GET['name']
    place_id = request.GET['placeid']
    r = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='+ place_id + '&key=' + getkey())
    r = r.json()
    addr = r['result']['formatted_address']
    name = r['result']['name']
    url = r['result']['url']

    if 'rating' in r['result']:
        rating = [r['result']['rating'],r['result']['user_ratings_total']]
    else:
        rating = ["Not Available",0]
    
    if 'reviews' in r['result']:
        reviews = r['result']['reviews']
    else:
        reviews = []

    reviews_lst = []

    for i in reviews:
        reviews_lst.append([i['author_name'],i['rating'],i['relative_time_description'],i['text']])


    categories = {'Bars' : "bar","Museuem" : "museum","Hospitals" : "hospital","Gym" : "gym", "Hotels" : "restaurant","Parks" : "park","Jwellery" : "jewelry_store" ,"Zoo" : "zoo"}
    filepath = os.path.join(django_settings.STATIC_ROOT + '/static/images', 'place.jpg')
    if 'photos' in r['result']:
        photo_ref = r['result']['photos'][0]['photo_reference']
        r2  = requests.get('https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference='+photo_ref +'&key=' + getkey())
        file=open(filepath, 'wb')
        for i in r2:
            if i:
                file.write(i)        
        file.close()
    elif os.path.exists(filepath):
        os.remove(filepath)

    return render(request,'place_detail.html',{"url" : url,"name" : name,"addr" : addr,"rating" : rating,"city_name" : city_name,"category" : categories,"reviews" : reviews_lst,"place_id" : place_id})

def addtoFav(request):
    name = request.user.username
    place_id = request.GET['placeid']
    city = request.GET['city']
    place_name = request.GET['place_name']

    if request.user.is_authenticated:
        exist = addToFav.objects.filter(name=name,place_id=place_id)   
        add = addToFav()
        add.name = name
        add.place_id = place_id
        add.place_name = place_name
        add.city_name = city
        if not exist:
            add.save()
        return redirect('/place?name=' + city + '&placeid='+ place_id)
    else:
        return redirect('/auth/login')
    
def see(request):
    if request.user.is_authenticated:
        fav_places = addToFav.objects.filter(name=request.user.username)
        return render(request, "favouriteplaces.html" ,{"places" : fav_places})
    else:
        return redirect('/auth/login')