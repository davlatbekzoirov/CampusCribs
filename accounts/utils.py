import secrets
from django.core.mail import EmailMessage
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from .models import EmailVerification

def generate_verification_token():
    """Generate a secure random token for email verification"""
    return secrets.token_urlsafe(32)

def send_verification_email(user, request):
    """Send verification email to user"""
    # Create or get verification record
    verification, created = EmailVerification.objects.get_or_create(user=user)
    verification.token = generate_verification_token()
    verification.is_verified = False
    verification.save()
    
    # Build verification URL
    verification_url = request.build_absolute_uri(
        reverse('verify_email', kwargs={'token': verification.token})
    )
    
    # Email content
    subject = 'Verify Your CampusCribs Email Address'
    message = f"""
Hello {user.first_name or user.username},

Welcome to CampusCribs! Please verify your email address by clicking the link below:

{verification_url}

This link will expire in 1 hour.

If you didn't create this account, please ignore this email.

Best regards,
CampusCribs Team
"""
    
    html_message = f"""
<html>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
            <h2 style="color: #534AB7;">Welcome to CampusCribs!</h2>
            <p>Hi {user.first_name or user.username},</p>
            <p>Thank you for registering! Please verify your email address by clicking the button below:</p>
            <p style="text-align: center; margin: 30px 0;">
                <a href="{verification_url}" style="background-color: #534AB7; color: white; padding: 12px 30px; text-decoration: none; border-radius: 5px; display: inline-block; font-weight: bold;">
                    Verify Email Address
                </a>
            </p>
            <p>Or copy and paste this link:</p>
            <p style="word-break: break-all; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                {verification_url}
            </p>
            <p style="color: #888; font-size: 12px;">This link will expire in 1 hour.</p>
            <hr style="border: none; border-top: 1px solid #eee;">
            <p style="color: #888; font-size: 12px;">If you didn't create this account, please ignore this email.</p>
            <p style="color: #888; font-size: 12px;">Best regards,<br><strong>CampusCribs Team</strong></p>
        </div>
    </body>
</html>
"""
    
    try:
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )
        email.attach_alternative(html_message, "text/html")
        email.send(fail_silently=False)
        print(f"✓ Verification email sent to {user.email}")
        return True
    except Exception as e:
        print(f"✗ Failed to send email to {user.email}: {str(e)}")
        return False

def verify_email_token(token):
    """Verify an email token and return user if valid"""
    try:
        verification = EmailVerification.objects.get(token=token)
        
        if verification.is_verified:
            return None, "Email already verified"
        
        if verification.is_token_expired():
            return None, "Verification link has expired"
        
        # Mark as verified
        verification.is_verified = True
        verification.verified_at = timezone.now()
        verification.save()
        
        # Mark user as active
        user = verification.user
        user.is_active = True
        user.save()
        
        return user, "Email verified successfully"
    
    except EmailVerification.DoesNotExist:
        return None, "Invalid verification link"
