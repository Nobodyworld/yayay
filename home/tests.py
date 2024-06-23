from django.test import TestCase
from django.urls import reverse
from .models import HomePageContent

class HomePageContentModelTest(TestCase):
    def setUp(self):
        HomePageContent.objects.create(title='Test Title', content='Test Content')

    def test_homepage_content(self):
        content = HomePageContent.objects.get(id=1)
        expected_object_name = f'{content.title}'
        self.assertEqual(expected_object_name, 'Test Title')
