import random

from django.core.management import BaseCommand
from django.db import transaction
from faker import Faker

from courses.models import Category, Tag


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        fake = Faker()
        tags_names = ["Advanced", "Basic", "Adult", "Free"]

        categories = ["Programming", "Testing", "Management",
                      "Business training", "Marketing", "Design", "English courses"]

        for category in categories:
            Category.objects.get_or_create(name=category)

        courses_list = []

        for i in range(10000):
            name = f"{fake.word()} {fake.word()}".title()
            category = Category.objects.order_by("?").first()
            price = random.randint(13000, 20000)
            lessons = random.randint(16, 40)
            duration = f"{int(lessons / 8)} months"
            courses_list.append(category.courses.create(name=name, course_price=price,
                                                        lessons_amount=lessons, duration=duration))

        tags = [Tag.objects.get_or_create(name=name)[0] for name in tags_names]

        for course in courses_list:
            random_tags = random.sample(tags, random.randint(1, 3))
            course.tags.add(*random_tags)
            course.save()

        self.stdout.write(self.style.SUCCESS("Successfully created 10000 courses with random tags."))
