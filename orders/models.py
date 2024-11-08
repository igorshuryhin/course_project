import uuid
from django.db import models, transaction
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from courses.models import Course


# Create your models here.
class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    courses = models.ManyToManyField(Course, through='OrderCourse')
    total_price = models.IntegerField(null=True)


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


@receiver(post_save, sender=OrderCourse)
def update_order_total_price(sender, instance, **kwargs):
    with transaction.atomic():
        order = instance.order
        order.total_price = sum([op.price for op in order.order_courses.all()])
        order.save()


@receiver(pre_save, sender=OrderCourse)
def update_order_product_price(sender, instance: OrderCourse, **kwargs):
    instance.price = instance.course.course_price
