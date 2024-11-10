import uuid
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

import time
from threading import Timer

from courses.models import Course


# Create your models here.
class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    courses = models.ManyToManyField(Course, through='OrderCourse')
    total_price = models.IntegerField(null=True)

    def finalize_order(self):
        # Calculate the total price
        self.total_price = sum(order_course.price for order_course in self.order_courses.all())
        self.save()

        # Send order creation email notification
        from orders.tasks import send_order_creation_email
        course_list = [order_course.course.name for order_course in self.order_courses.all()]
        send_order_creation_email.delay(self.user.username, self.user.email, self.pk, course_list, self.total_price)


@receiver(post_save, sender=Order)
def order_create_signal(sender, instance, created, **kwargs):
    if created:
        from orders.tasks import send_order_creation_notification, update_orders_report, update_order_totals_report
        send_order_creation_notification.delay(instance.pk)
        update_orders_report.delay()
        update_order_totals_report.delay()


class OrderCourse(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def delayed_finalize(order):
    time.sleep(2)  # Delay to allow for all OrderCourses to be added
    if order.order_courses.exists():  # Ensure there are OrderCourses before finalizing
        order.finalize_order()


@receiver(post_save, sender=OrderCourse)
def update_order_total_price(sender, instance, created, **kwargs):
    if created:
        order = instance.order
        order_total_price = sum(order_course.price for order_course in order.order_courses.all())
        order.total_price = order_total_price
        order.save()

        # Start a delayed call to finalize the order
        Timer(2.0, delayed_finalize, [order]).start()


@receiver(pre_save, sender=OrderCourse)
def update_order_product_price(sender, instance: OrderCourse, **kwargs):
    instance.price = instance.course.course_price
