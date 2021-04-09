from django.test import TestCase

from .models import *


class UserTestCase(TestCase):

    def setUp(self):
        addToFav.objects.create(name="rajkalathiya699@gmail.com", place_name="Pratap Garder", city_name="Surat", place_id = "aknbdj648adk")
        
    def testPlaceDetail(self):
        obj = addToFav.objects.get(name="rajkalathiya699@gmail.com")
        self.assertEqual(obj.city_name,"Surat")

        