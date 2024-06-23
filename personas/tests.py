from django.test import TestCase
from django.urls import reverse
from .models import Persona
from django.contrib.auth import get_user_model

class PersonaTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.persona = Persona.objects.create(user=self.user, name='Test Persona', description='Test Description', public=True)

    def test_personas_list_view(self):
        response = self.client.get(reverse('personas:personas_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Persona')

    def test_persona_detail_view(self):
        response = self.client.get(reverse('personas:persona_detail', args=[self.persona.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Persona')

    def test_create_persona_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('personas:create_persona'), {
            'name': 'New Persona',
            'description': 'New Description',
            'public': True,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Persona.objects.filter(name='New Persona').exists())
