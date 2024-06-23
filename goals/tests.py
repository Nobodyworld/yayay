# goals/tests.py
from django.test import TestCase
from django.urls import reverse

class GoalsTests(TestCase):
    def test_set_goals_page(self):
        response = self.client.get(reverse('set_goals'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Set Goals')
