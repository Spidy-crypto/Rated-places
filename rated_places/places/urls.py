from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('category',views.category),
    path('places',views.places)
]