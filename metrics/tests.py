from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import PersonaMetrics, Skill, Attribute, SkillLevel, AttributeLevel
from personas.models import Persona
import factory
from faker import Faker

User = get_user_model()
fake = Faker()

class PersonaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Persona

    name = factory.LazyAttribute(lambda _: fake.name())
    creator = factory.SubFactory('yourapp.factories.UserFactory')

class PersonaMetricsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.persona = PersonaFactory(creator=self.user)
        self.metrics = PersonaMetrics.objects.create(persona=self.persona)

    def test_update_metrics(self):
        self.metrics.update_metrics(points=10, upvote=True)
        self.metrics.refresh_from_db()
        self.assertEqual(self.metrics.total_points, 10)
        self.assertEqual(self.metrics.total_upvotes, 1)
    
    def test_update_rating(self):
        self.metrics.update_rating(4)
        self.metrics.refresh_from_db()
        self.assertEqual(self.metrics.average_rating, 4)

class AttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attribute

    name = factory.LazyAttribute(lambda _: fake.word())
    description = factory.LazyAttribute(lambda _: fake.text())

class SkillFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Skill

    name = factory.LazyAttribute(lambda _: fake.word())
    attribute = factory.SubFactory(AttributeFactory)

class SkillLevelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SkillLevel

    persona = factory.SubFactory(PersonaFactory)
    skill = factory.SubFactory(SkillFactory)

class AttributeSkillTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.persona = PersonaFactory(creator=self.user)
        self.attribute = AttributeFactory()
        self.skill = SkillFactory(attribute=self.attribute)
        self.skill_level = SkillLevelFactory(persona=self.persona, skill=self.skill)

    def test_add_experience_to_skill(self):
        self.skill_level.add_experience(150)
        self.skill_level.refresh_from_db()
        self.assertEqual(self.skill_level.level, 2)
        self.assertEqual(self.skill_level.experience_points, 50)

    def test_update_attribute_level(self):
        self.attribute_level = AttributeLevel.objects.create(persona=self.persona, attribute=self.attribute)
        self.attribute_level.update_total_points()
        self.attribute_level.refresh_from_db()
        self.assertEqual(self.attribute_level.total_points, 150) # Assuming persona has 150 points in that attribute
