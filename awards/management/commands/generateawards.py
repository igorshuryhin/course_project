from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction
import faker

from awards.models import Award


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        fake = faker.Faker()
        user = User.objects.create(username=fake.name(), email=fake.email())

        for _ in range(100):
            name = fake.word().title()
            Award.objects.create(name=name, user=user)
