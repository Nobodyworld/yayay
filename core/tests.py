from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Badge, Feedback, PrivateFeedback, Listing, Review

class CoreTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')

    def test_landing_page_view(self):
        response = self.client.get(reverse('core:landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to My Project')

    def test_register_view(self):
        response = self.client.get(reverse('core:register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register')
