from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import EmailVerification

@receiver(post_save, sender=User)
def create_email_verification(sender, instance, created, **kwargs):
    """Create EmailVerification record when user is created"""
    if created:
        EmailVerification.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_email_verification(sender, instance, **kwargs):
    """Ensure EmailVerification record exists"""
    if hasattr(instance, 'email_verification'):
        instance.email_verification.save()
