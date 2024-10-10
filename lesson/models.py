from django.db import models
from homework.models import Homework

# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    notes = models.TextField(null=True, blank=True)
    homework = models.OneToOneField(Homework, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
