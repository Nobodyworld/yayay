from django.urls import path
from .views import (
    PromptsListView, PromptsDetailView, PromptsCreateView, 
    PromptsUpdateView, PromptsDeleteView
)

app_name = 'prompts'

urlpatterns = [
    path('', PromptsListView.as_view(), name='prompts_list'),
    path('<int:pk>/', PromptsDetailView.as_view(), name='prompts_detail'),
    path('create/', PromptsCreateView.as_view(), name='prompts_create'),
    path('<int:pk>/update/', PromptsUpdateView.as_view(), name='prompts_update'),
    path('<int:pk>/delete/', PromptsDeleteView.as_view(), name='prompts_delete'),
]
