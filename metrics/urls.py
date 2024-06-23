from django.urls import path
from . import views

app_name = 'metrics'

urlpatterns = [
    path('persona/<int:persona_id>/', views.persona_metrics, name='persona_metrics'),
    path('persona/<int:persona_id>/detail/', views.PersonaMetricsDetailView.as_view(), name='persona_metrics_detail'),
    path('skills/', views.MetricsListView.as_view(), name='skills_list'),
    path('skills/<int:pk>/', views.MetricsDetailView.as_view(), name='skill_detail'),
    path('analytics/', views.analytics_dashboard, name='analytics_dashboard'),
    path('attributes/', views.AttributeListView.as_view(), name='attributes_list'),
    path('attributes/<int:pk>/', views.AttributeDetailView.as_view(), name='attribute_detail'),
]
