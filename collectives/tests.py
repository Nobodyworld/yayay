from django.test import TestCase
from django.urls import reverse
from .models import Collective
from django.contrib.auth import get_user_model

class CollectiveTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.collective = Collective.objects.create(name='Test Collective', description='Test Description')

    def test_collectives_list_view(self):
        response = self.client.get(reverse('collectives:collectives_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Collective')

    def test_collective_detail_view(self):
        response = self.client.get(reverse('collectives:collective_detail', args=[self.collective.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Collective')
