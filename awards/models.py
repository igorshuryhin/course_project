from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Award(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Award)
def create_award(sender, instance, created, **kwargs):
    if created:
        from awards.tasks import send_new_award_notification
        send_new_award_notification.delay(instance.pk)
