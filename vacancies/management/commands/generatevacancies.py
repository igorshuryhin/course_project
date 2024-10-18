import random

from django.core.management import BaseCommand
from django.db import transaction
from faker import Faker

from vacancies.models import Type, Tag


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        faker = Faker()

        types_names = ['Remoted', 'In office']
        tags_names = [faker.word().title() for _ in range(10)]

        for name in types_names:
            Type.objects.get_or_create(name=name)

        vacancies = []

        for _ in range(1000):
            name = f"{faker.word()} {faker.word()}".title()
            vac_type = Type.objects.order_by("?").first()

            vacancies.append(vac_type.vacancies.create(name=name, type=vac_type))

        tags = [Tag.objects.get_or_create(name=name)[0] for name in tags_names]

        for vac in vacancies:
            random_tags = random.sample(tags, random.randint(1, 3))
            vac.tags.add(*random_tags)
            vac.save()

        self.stdout.write(self.style.SUCCESS("Successfully created 1000 vacancies with random tags."))
