import factory
from MySite.apps.users.models import CustomUser
from MySite.apps.chat.models import Topic, Message
from rest_framework.authtoken.models import Token


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Faker('first_name')
    password = 'qwerty123456'
    email = factory.Faker('email')
    date_of_birth = factory.Faker('date')


class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Topic

    owner = factory.SubFactory(UserFactory)
    name = factory.Faker('sentence', nb_words=3)
    slug = factory.Faker('sentence', nb_words=3)


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    owner = factory.SubFactory(UserFactory)
    topic = factory.SubFactory(TopicFactory)
    text = factory.Faker('sentence', nb_word=10)


class TokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Token

    user = factory.SubFactory(UserFactory)
