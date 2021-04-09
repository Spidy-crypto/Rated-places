from django.test import TestCase

from django.contrib.auth.models import User

class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create(email = "rajkalathiya123@gmail.com", password = "raj123", id="1")

    def testUserDetail(self):
        user = User.objects.get(email = "rajkalathiya123@gmail.com")
        self.assertEqual(user.id,1)

        