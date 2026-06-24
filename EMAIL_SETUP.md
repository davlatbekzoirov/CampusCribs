# Email Verification Setup Guide for CampusCribs

## Issue Found
Your Django project was **missing all email configuration**. No SMTP settings, no email sending logic, and no verification system.

## What Was Fixed

### 1. **settings.py** - Added Email Configuration
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # ⚠️ UPDATE THIS
EMAIL_HOST_PASSWORD = 'your-app-password'  # ⚠️ UPDATE THIS
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

### 2. **models.py** - Added EmailVerification Model
- Stores verification tokens per user
- Tracks verification status
- Auto-expires tokens after 1 hour

### 3. **utils.py** - Added Email Sending Functions
- `send_verification_email()` - Sends HTML email with verification link
- `verify_email_token()` - Validates token and marks email as verified
- `generate_verification_token()` - Creates secure random tokens

### 4. **signals.py** - Added Signal Handlers
- Auto-creates EmailVerification record when user registers
- Ensures data consistency

### 5. **views.py** - Updated Registration Flow
- Users now inactive until email verified
- Sends verification email on registration
- Added email verification endpoint
- Login blocked until email verified

### 6. **urls.py** - Added Verification Endpoint
- Added `/verify-email/<token>/` route

---

## Setup Steps

### Step 1: Generate Gmail App Password
1. Go to https://myaccount.google.com/security
2. Enable **2-Step Verification** (if not already)
3. Go to **App passwords** 
4. Select **Mail** and **Windows Computer**
5. Copy the 16-character password

### Step 2: Update settings.py
Replace these values in `core/settings.py`:
```python
EMAIL_HOST_USER = 'your-gmail@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'xxxx xxxx xxxx xxxx'  # 16-char app password
```

### Step 3: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Test Email Sending
```bash
python manage.py shell
```

```python
from django.core.mail import send_mail
send_mail(
    'Test Email',
    'This is a test.',
    'your-email@gmail.com',
    ['recipient@example.com'],
)
```

---

## How It Works

### Registration Flow
```
1. User registers
2. Account created but is_active = False
3. Verification email sent to user
4. User clicks link in email
5. /verify-email/<token>/ endpoint validates token
6. User marked as verified
7. User can now log in
```

### Email Sending
- Uses Django's `EmailMessage` class
- Sends both plain text and HTML versions
- Includes clickable verification button
- Token expires after 1 hour (configurable in settings)

---

## Troubleshooting

### Email Not Sending?
```bash
# Test SMTP connection
python manage.py shell
from django.core.mail import get_connection
conn = get_connection()
conn.open()
conn.close()
```

### Common Issues
- ❌ **"App password not working"** → Regenerate in Google Account
- ❌ **"SMTP Connection Refused"** → Verify EMAIL_HOST and EMAIL_PORT
- ❌ **"Less secure apps"** → Use App Passwords, not regular password
- ❌ **"SSL certificate error"** → Already handled with EMAIL_USE_TLS = True

---

## Files Modified/Created
- ✅ `core/settings.py` - Email config
- ✅ `accounts/models.py` - EmailVerification model
- ✅ `accounts/views.py` - Verification views
- ✅ `accounts/urls.py` - Verification endpoint
- ✅ `accounts/utils.py` - Email sending functions (NEW)
- ✅ `accounts/signals.py` - Signal handlers (NEW)
- ✅ `accounts/apps.py` - Signal registration
- ✅ `accounts/admin.py` - Admin interface

---

## Next Steps (Optional)
- Add resend email functionality
- Send welcome email on verification
- Add password reset via email
- Email notification for important events
