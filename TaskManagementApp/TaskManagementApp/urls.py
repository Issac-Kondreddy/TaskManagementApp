from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('TaskManager.urls')),  # Include TaskManager URLs
    path('auth/', include('UserAuthentication.urls')),  # Include UserAuthentication URLs
    path('api/', include('TaskManager.api_urls')),
]
