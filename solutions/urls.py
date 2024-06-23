from django.urls import path
from . import views

app_name = 'solutions'

urlpatterns = [
    path('create/', views.create_solution, name='create_solution'),
]
