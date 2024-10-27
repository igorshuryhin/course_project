from datetime import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models.signals import m2m_changed


class Grade(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


class Homework(models.Model):
    name = models.CharField(max_length=255)
    deadline = models.DateField(null=True, blank=True)
    retakes_amount = models.IntegerField(null=True, blank=True)
    complexity = models.IntegerField(null=True, blank=True)
    passed_amount = models.IntegerField(null=True, blank=True)
    avg_grade = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    grades = models.ManyToManyField(Grade, blank=True, related_name='homeworks')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@receiver(m2m_changed, sender=Homework.grades.through)
def update_avg_grade(sender, instance, action, **kwargs):
    if action == "post_add":
        grades = list(instance.grades.all())
        grades_values = [grade.grade for grade in grades]

        if grades_values:
            avg_grade = int(sum(grades_values) / len(grades_values))
            instance.avg_grade = avg_grade
            instance.save(update_fields=['avg_grade'])
        else:
            if instance.avg_grade is not None:  # Avoid unnecessary saves
                instance.avg_grade = None
                instance.save(update_fields=['avg_grade'])