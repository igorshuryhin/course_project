from django.contrib.auth.models import User
from django.db import models


class TelegramUserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.IntegerField()
