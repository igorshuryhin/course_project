from django.db import models
from homework.models import Homework

# Create your models here.

class Attendance(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    present = models.BooleanField(default=False)

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    notes = models.TextField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    homework = models.OneToOneField(Homework, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
