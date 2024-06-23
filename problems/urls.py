from django.urls import path
from . import views

app_name = 'problems'

urlpatterns = [
    path('identify/', views.identify_problems, name='identify_problems'),
]
