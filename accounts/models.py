from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class EmailVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='email_verification')
    token = models.CharField(max_length=100, unique=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    
    def is_token_expired(self):
        from django.conf import settings
        timeout = getattr(settings, 'EMAIL_VERIFICATION_TIMEOUT', 3600)
        return timezone.now() > self.created_at + timedelta(seconds=timeout)
    
    def __str__(self):
        return f"Email verification for {self.user.username}"
