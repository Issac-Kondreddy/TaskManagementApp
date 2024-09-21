from django.urls import path
from . import views

urlpatterns = [
    path('login-signup/', views.auth_view, name='auth'),
    path('auth/logout/', views.logout_view, name='logout'),
]
