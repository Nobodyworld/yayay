from django.urls import path
from . import views

app_name = 'artifacts'

urlpatterns = [
    path('', views.artifacts_list, name='artifacts_list'),
    path('<int:artifact_id>/', views.artifact_detail, name='artifact_detail'),
    path('upload/', views.artifact_upload, name='artifact_upload'),
    path('<int:artifact_id>/delete/', views.artifact_delete, name='artifact_delete'),
    path('<int:artifact_id>/download/', views.artifact_download, name='artifact_download'),
]
