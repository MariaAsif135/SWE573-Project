from django.test import TestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User



class Unit_Tests_For_Application(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="unittest", email="testing123@testing.com",password="password")
        self.user.save()

    def Signing_In_Unittest(self):
        user = authenticate(username='unittest', password='password')
        self.assertTrue((user is not None) and user.is_authenticated)

    def Signing_In_With_Wrong_Username_Unittest(self):
        user = authenticate(username='unittestwow', password='password')
        self.assertFalse(user is not None and user.is_authenticated)

    def Signing_In_With_Wrong_Password_Unittest(self):
        user = authenticate(username='unittest', password='passwordqwerty')
        self.assertFalse(user is not None and user.is_authenticated)

    


# Create your tests here.
