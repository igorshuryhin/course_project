from datetime import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Grade(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


class Homework(models.Model):
    name = models.CharField(max_length=255)
    deadline = models.DateField()
    retakes_amount = models.IntegerField()
    complexity = models.IntegerField()
    passed_amount = models.IntegerField()
    avg_grade = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    description = models.TextField(null=True, blank=True)

    grade = models.ForeignKey(Grade, null=True, blank=True, related_name="homeworks", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
