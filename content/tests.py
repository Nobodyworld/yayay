from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from faker import Faker
from personas.models import Persona
from .models import PersonaChat, PersonaImage

User = get_user_model()
fake = Faker()

class PersonaChatViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.persona = Persona.objects.create(name='Test Persona', creator=self.user)
        self.chat = PersonaChat.objects.create(persona=self.persona, content='Test Chat', is_public=True)
        self.client.login(username='testuser', password='testpass123')

    def test_add_chat_view(self):
        response = self.client.post(reverse('content:create_chat'), {'content': 'Hello World', 'is_public': True, 'persona': self.persona.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(PersonaChat.objects.count(), 2)
        self.assertEqual(PersonaChat.objects.last().content, 'Hello World')

    def test_chat_detail_view(self):
        response = self.client.get(reverse('content:chat_detail', args=[self.chat.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.chat.content)

class PersonaImageViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.persona = Persona.objects.create(name='Test Persona', creator=self.user)
        self.image = PersonaImage.objects.create(persona=self.persona, caption='Test Image', image='path/to/image.jpg', is_public=True)
        self.client.login(username='testuser', password='testpass123')

    def test_add_image_view(self):
        image_content = SimpleUploadedFile('test_image.jpg', b'file_content', content_type='image/jpeg')
        response = self.client.post(reverse('content:create_image'), {'caption': 'Hello Image', 'is_public': True, 'image': image_content, 'persona': self.persona.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(PersonaImage.objects.count(), 2)
        self.assertEqual(PersonaImage.objects.last().caption, 'Hello Image')

    def test_image_detail_view(self):
        response = self.client.get(reverse('content:image_detail', args=[self.image.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.image.caption)
