from django.urls import path
from . import views

app_name = 'possessions'

urlpatterns = [
    path('', views.possessions_list, name='possessions_list'),
    path('create/', views.create_possession, name='create_possession'),
    path('<int:possession_id>/update/', views.update_possession, name='update_possession'),
    path('<int:possession_id>/delete/', views.delete_possession, name='delete_possession'),
]
