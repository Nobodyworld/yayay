from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register/', views.register, name='register'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-will/', views.create_will, name='create_will'),
    path('create-meaning/<int:will_id>/', views.create_meaning, name='create_meaning'),
    path('create-knowledge/<int:meaning_id>/', views.create_knowledge, name='create_knowledge'),
    path('create-wisdom/<int:knowledge_id>/', views.create_wisdom, name='create_wisdom'),
]
