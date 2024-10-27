import random
from faker import Faker
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction
from homework.models import Homework, Grade


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(1000):

            homework = Homework(
                name=f"{fake.word()} {fake.word()} Homework".title(),
                deadline=fake.date_between(start_date="today", end_date="+30d"),
                retakes_amount=random.randint(0, 3),
                complexity=random.randint(1, 3),
                passed_amount=random.randint(0, 20),
                description=fake.text(max_nb_chars=200),
            )
            homework.save()

            grades_list = []
            for i in range(random.randint(1, 3)):
                unique_username = f"{fake.user_name()}_{random.randint(1000, 9999)}"
                user = User.objects.create(username=unique_username, email=fake.email())
                grade_value = random.randint(1, 100)
                grade = Grade.objects.create(user=user, grade=grade_value)
                grades_list.append(grade)

            homework.grades.add(*grades_list)

            homework.refresh_from_db()

        self.stdout.write(self.style.SUCCESS("Successfully created 1000 homeworks!"))
