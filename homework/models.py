from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)