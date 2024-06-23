import factory
from django.contrib.auth import get_user_model
from faker import Faker
from content.models import Persona, PersonaChat, PersonaFeed
from social.models import Tag, Category, Post, Comment
from core.models import LandingPage, ChatFeed, ImageFeed, PromptsFeed
from metrics.models import Attribute, Skill, SkillLevel


User = get_user_model()
fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user_{n}')
    email = factory.LazyAttribute(lambda _: fake.email())
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=6))
    content = factory.LazyAttribute(lambda _: fake.text())
    author = factory.SubFactory(UserFactory)

class PersonaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Persona

    name = factory.LazyAttribute(lambda _: fake.name())
    creator = factory.SubFactory(UserFactory)

class PersonaChatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PersonaChat

    persona = factory.SubFactory(PersonaFactory)
    content = factory.LazyAttribute(lambda _: fake.text())

class PersonaFeedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PersonaFeed

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=6))
    user = factory.SubFactory(UserFactory)
    persona = factory.SubFactory(PersonaFactory)
    post = factory.SubFactory(PostFactory)

class ChatFeedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ChatFeed

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=6))
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    persona = factory.SubFactory(PersonaFactory)

class ImageFeedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ImageFeed

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=6))
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    persona = factory.SubFactory(PersonaFactory)

class PromptsFeedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PromptsFeed

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=6))
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)

class LandingPageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LandingPage

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=6))
    content = factory.LazyAttribute(lambda _: fake.text())

class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.LazyAttribute(lambda _: fake.word())
    slug = factory.Sequence(lambda n: f'tag-{n}')

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.LazyAttribute(lambda _: fake.word())
    slug = factory.Sequence(lambda n: f'category-{n}')

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.LazyAttribute(lambda _: fake.text())
    author = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)

class AttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attribute

    name = factory.LazyAttribute(lambda _: fake.word())

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
    level = 1
    experience_points = 0

    @factory.post_generation
    def handle_experience(self, create, extracted, **kwargs):
        if extracted:
            self.experience_points += extracted
            while self.experience_points >= 100:
                self.level += 1
                self.experience_points -= 100
            self.save()
