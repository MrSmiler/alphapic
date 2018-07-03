from django.test import TestCase
from home.models import User
from django.urls import reverse




class UserLoginTests(TestCase):

    def test_user_login(self):
        username = 'mrsmiler'
        password = '0n7e7vo1H'
        response = self.client.post(
                '/account/login/',
                {'username':username,'password':password},
                follow=True)

        self.assertEqual(response.status_code, 200)

       
                 
