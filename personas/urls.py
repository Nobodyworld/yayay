from django.urls import path
from . import views

app_name = 'personas'

urlpatterns = [
    path('', views.personas_list, name='personas_list'),
    path('<int:persona_id>/', views.persona_detail, name='persona_detail'),
    path('create/', views.create_persona, name='create_persona'),
    path('<int:persona_id>/update/', views.update_persona, name='update_persona'),
]
