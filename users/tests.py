# users/tests.py
from django.test import TestCase
from django.urls import reverse

class UserRegistrationTests(TestCase):
    def test_registration_page(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register')
