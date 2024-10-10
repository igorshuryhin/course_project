from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    vacancy_type = models.ManyToManyField(Type, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name