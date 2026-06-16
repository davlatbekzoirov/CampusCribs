from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('budget.urls')),
    path('roomieratio/', include('roomieratio.urls')),
    path('housing/', include('housing.urls')),
]
