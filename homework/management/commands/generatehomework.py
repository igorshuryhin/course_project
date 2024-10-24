import random

import faker
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction

from homework.models import Homework, Grade


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **kwargs):
        fake = faker.Faker()
        user = User.objects.create(username=fake.name(), email=fake.email())



        for _ in range(1000):
            grade = Grade.objects.create(user=user, grade=random.randint(1, 100))
            name = f"{fake.word()} {fake.word()} Homework".title()
            deadline = fake.date_between(start_date="today", end_date="+30d")
            retakes_amount = random.randint(0, 3)
            complexity = random.randint(1, 3)
            passed_amount = random.randint(0, 20)
            avg_grade = random.randint(0, 100)
            description = fake.text(max_nb_chars=200)

            grade.homeworks.create(name=name,
                deadline=deadline,
                retakes_amount=retakes_amount,
                complexity=complexity,
                passed_amount=passed_amount,
                avg_grade=avg_grade,
                description=description)

        self.stdout.write(self.style.SUCCESS(f"Successfully created 1000 homeworks!"))