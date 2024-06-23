from django.test import TestCase
from django.urls import reverse
from .models import Prompts, Category
from ztests.factories import UserFactory, TagFactory, CategoryFactory
from social.models import Tag

class ClassificationTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
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

class PromptsTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.prompts = Prompts.objects.create(
            text='Initial Prompts',
            author=self.user,
            rating=3
        )

    def test_prompts_list_view(self):
        response = self.client.get(reverse('prompts:prompts_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.prompts.text)

    def test_prompts_detail_view(self):
        response = self.client.get(reverse('prompts:prompts_detail', args=[self.prompts.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.prompts.text)

    def test_prompts_create_view(self):
        self.client.login(username=self.user.username, password='testpass123')
        response = self.client.post(reverse('prompts:prompts_create'), {
            'text': 'New Prompts Description',
            'author': self.user.id,
            'rating': 5
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Prompts.objects.filter(text='New Prompts Description').exists())

    def test_prompts_edit_view(self):
        self.client.login(username=self.user.username, password='testpass123')
        response = self.client.post(reverse('prompts:prompts_edit', args=[self.prompts.id]), {
            'text': 'Updated Prompts Description',
            'author': self.user.id,
            'rating': 5
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Prompts.objects.filter(text='Updated Prompts Description').exists())

    def test_prompts_delete_view(self):
        self.client.login(username=self.user.username, password='testpass123')
        response = self.client.post(reverse('prompts:prompts_delete', args=[self.prompts.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Prompts.objects.filter(text=self.prompts.text).exists())
