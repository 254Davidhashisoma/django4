from django.db.models.signals import post_save
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()