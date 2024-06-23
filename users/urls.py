from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
]
