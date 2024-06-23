from django.urls import path
from . import views

app_name = 'leveling'

urlpatterns = [
    path('attributes/', views.AttributeListView.as_view(), name='attributes_list'),
    path('attributes/<int:pk>/', views.AttributeDetailView.as_view(), name='attribute_detail'),
    path('skills/', views.SkillListView.as_view(), name='skills_list'),
    path('skills/<int:pk>/', views.SkillDetailView.as_view(), name='skill_detail'),
]
