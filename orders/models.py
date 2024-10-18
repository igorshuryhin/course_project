import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from courses.models import Course


# Create your models here.
class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ManyToManyField(Course, through='OrderCourse')

class OrderCourse(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

@receiver(pre_save, sender=OrderCourse)
def update_order_price(sender, instance, **kwargs):
    instance.price = instance.course.course_price