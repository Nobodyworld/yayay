# File: problems/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Problem
from goals.models import Goal
from django.contrib.auth import get_user_model

User = get_user_model()

class ProblemTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.goal = Goal.objects.create(user=self.user, title='Test Goal')
        self.problem = Problem.objects.create(goal=self.goal, title='Test Problem', description='Test Description')

    def test_identify_problems_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('problems:identify_problems'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Identify Problems')

    def test_create_problem(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('problems:identify_problems'), {
            'title': 'New Problem',
            'description': 'New Description',
            'goal': self.goal.id  # Make sure to pass the goal id
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Problem.objects.filter(title='New Problem').exists())

    def test_create_problem_without_login(self):
        response = self.client.post(reverse('problems:identify_problems'), {
            'title': 'Unauthorized Problem',
            'description': 'Unauthorized Description'
        })
        self.assertNotEqual(response.status_code, 302)
        self.assertFalse(Problem.objects.filter(title='Unauthorized Problem').exists())
