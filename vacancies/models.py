from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey(Type, blank=True, null=True, related_name="vacancies", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Vacancy)
def vacancy_create_signal(sender, instance, created, **kwargs):
    if created:
        from vacancies.tasks import report_vacancies_on_google_sheets
        report_vacancies_on_google_sheets.delay()
