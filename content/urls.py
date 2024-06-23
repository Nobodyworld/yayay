# content/urls.py

from django.urls import path
from .views import (
    PersonaChatCreateView, PersonaChatDetailView, PersonaChatListView,
    PersonaImageCreateView, PersonaImageDetailView, PersonaImageListView, select_persona
)
from home.views import content_home  # Ensure this import works

app_name = 'content'

urlpatterns = [
    path('', content_home, name='content_home'),
    path('select/', select_persona, name='select_persona'),
    path('chat/create/', PersonaChatCreateView.as_view(), name='create_chat'),  # Ensure this name is correct
    path('chat/<int:pk>/', PersonaChatDetailView.as_view(), name='chat_detail'),
    path('chats/', PersonaChatListView.as_view(), name='chat_list'),
    path('image/create/', PersonaImageCreateView.as_view(), name='create_image'),
    path('image/<int:pk>/', PersonaImageDetailView.as_view(), name='image_detail'),
    path('images/', PersonaImageListView.as_view(), name='image_list'),
]
