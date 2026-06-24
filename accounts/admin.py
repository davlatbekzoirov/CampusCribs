from django.contrib import admin
from .models import EmailVerification

@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_verified', 'created_at', 'verified_at')
    list_filter = ('is_verified', 'created_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('token', 'created_at', 'verified_at')
