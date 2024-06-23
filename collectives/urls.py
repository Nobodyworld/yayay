from django.urls import path
from . import views

app_name = 'collectives'

urlpatterns = [
    path('', views.collectives_list, name='collectives_list'),
    path('<int:collective_id>/', views.collective_detail, name='collective_detail'),
    path('create/', views.create_collective, name='create_collective'),
    path('join/', views.join_collective, name='join_collective'),
]
