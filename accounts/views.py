from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm
from .utils import send_verification_email, verify_email_token

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False  # Require email verification
        user.save()
        
        # Send verification email
        if send_verification_email(user, request):
            return render(request, 'accounts/verify_email.html', {
                'user_email': user.email
            })
        else:
            messages.error(request, 'Failed to send verification email. Please try again.')
            user.delete()
    
    return render(request, 'accounts/auth.html', {'form': form, 'mode': 'register'})

@require_http_methods(["GET"])
def verify_email_view(request, token):
    """Verify email from token in URL"""
    user, message = verify_email_token(token)
    
    if user:
        return render(request, 'accounts/verification_success.html', {
            'user': user
        })
    else:
        messages.error(request, f"✗ {message}")
        return redirect('register')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        if not user.is_active:
            messages.error(request, 'Please verify your email before logging in.')
            return redirect('login')
        login(request, user)
        return redirect(request.GET.get('next', 'dashboard'))
    return render(request, 'accounts/auth.html', {'form': form, 'mode': 'login'})

def logout_view(request):
    logout(request)
    return redirect('login')