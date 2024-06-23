from django.test import TestCase
from django.urls import reverse
from .models import Category, Tag, Post, Notification
from django.contrib.auth import get_user_model
from ztests.factories import UserFactory, CategoryFactory, TagFactory, PostFactory
import factory
from faker import Faker

User = get_user_model()
fake = Faker()

class ClassificationTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory(password='testpass123')
        self.category = CategoryFactory()
        self.tag = TagFactory()

    def test_create_tag(self):
        self.client.login(username=self.user.username, password='testpass123')
        response = self.client.post(reverse('social:tag_create'), {'name': 'NewTag'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 2)
        self.assertTrue(Tag.objects.filter(name='NewTag').exists())

    def test_create_category(self):
        self.client.login(username=self.user.username, password='testpass123')
        response = self.client.post(reverse('social:category_create'), {'name': 'NewCategory'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Category.objects.count(), 2)
        self.assertTrue(Category.objects.filter(name='NewCategory').exists())

class PostTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory(password='testpass123')
        self.post = PostFactory(author=self.user)

    def test_post_detail_view(self):
        self.client.login(username=self.user.username, password='testpass123')
        response = self.client.get(reverse('social:post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.content)

class NotificationTests(TestCase):
    def setUp(self):
        self.user = UserFactory(password='testpass123')
        self.notification = Notification.objects.create(user=self.user, message='Test notification')

    def test_notification_creation(self):
        self.assertEqual(self.notification.message, 'Test notification')
        self.assertFalse(self.notification.is_read)

    def test_notification_list_view(self):
        self.client.login(username=self.user.username, password='testpass123')
        response = self.client.get(reverse('social:notification_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test notification')
