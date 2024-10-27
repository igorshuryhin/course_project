import random
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from homework.models import Homework
from lesson.models import Lesson


class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **kwargs):
        fake = Faker()
        available_homeworks = list(
            Homework.objects.filter(lesson__isnull=True))  # Get homeworks that aren't already assigned

        for _ in range(1000):
            name = f"{fake.word()} {fake.word()} Lesson".title()
            date = fake.date_between(start_date="today", end_date="+30d")
            notes = fake.text(max_nb_chars=200)
            video = fake.url()

            homework = available_homeworks.pop() if available_homeworks and random.choice([True, False]) else None

            Lesson.objects.get_or_create(
                name=name,
                date=date,
                notes=notes,
                video=video,
                homework=homework
            )

        self.stdout.write(self.style.SUCCESS("Successfully created 1000 lessons!"))
