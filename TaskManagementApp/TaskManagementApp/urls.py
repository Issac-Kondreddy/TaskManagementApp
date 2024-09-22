from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/tasks/')),  # Redirect root URL to tasks
    path('tasks/', include('TaskManager.urls')),  # Include TaskManager URLs
    path('auth/', include('UserAuthentication.urls')),  # Include UserAuthentication URLs
    path('api/', include('TaskManager.api_urls')),  # Include API URLs
]
