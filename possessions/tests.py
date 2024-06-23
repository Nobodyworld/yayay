from django.test import TestCase
from django.urls import reverse
from .models import Possession
from django.contrib.auth import get_user_model

class PossessionTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.possession = Possession.objects.create(
            user=self.user,
            name='Test Possession',
            description='Test Description'
        )

    def test_possessions_list_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('possessions:possessions_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Possession')

    def test_create_possession_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('possessions:create_possession'), {
            'name': 'New Possession',
            'description': 'New Description'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Possession.objects.filter(name='New Possession').exists())

    def test_update_possession_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('possessions:update_possession', args=[self.possession.id]), {
            'name': 'Updated Possession',
            'description': 'Updated Description'
        })
        self.assertEqual(response.status_code, 302)
        self.possession.refresh_from_db()
        self.assertEqual(self.possession.name, 'Updated Possession')

    def test_delete_possession_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('possessions:delete_possession', args=[self.possession.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Possession.objects.filter(id=self.possession.id).exists())
