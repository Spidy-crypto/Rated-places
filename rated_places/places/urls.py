from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('category',views.category),
    path('places',views.places),
    path('place',views.place_detail),
    path('fav',views.addtoFav),
    path('seefavouriteplace',views.see),
    path('remove/<str:name>/<str:place_id>',views.remove)
]