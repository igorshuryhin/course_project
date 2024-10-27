from django.core.management import BaseCommand
from django.db import transaction
from django.contrib.auth.models import User
import faker

from courses.models import Course
from orders.models import Order, OrderCourse


class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.fake = faker.Faker()
        self.existing_usernames = set()

    def generate_unique_username(self):
        while True:
            username = self.fake.user_name()
            if username not in self.existing_usernames:
                self.existing_usernames.add(username)
                return username

    def create_order(self):
        username = self.generate_unique_username()
        user = User.objects.create_user(username=username, email=self.fake.email())

        order = Order.objects.create(user=user)

        course_ids = Course.objects.values_list('id', flat=True)

        if course_ids:
            course_id = self.fake.random_element(course_ids)
            OrderCourse.objects.create(
                order=order,
                course_id=course_id,
            )

    @transaction.atomic
    def handle(self, *args, **options):
        for _ in range(100):
            self.create_order()
