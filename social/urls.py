from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
    path('tags/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('notifications/', views.NotificationListView.as_view(), name='list_notifications'),
    path('notifications/<int:pk>/read/', views.NotificationReadView.as_view(), name='read_notification'),
    path('notifications/<int:pk>/delete/', views.NotificationDeleteView.as_view(), name='delete_notification'),
    path('follow/<int:followed_user_id>/', views.FollowView.as_view(), name='follow'),
    path('posts/', views.PostListView.as_view(), name='list_posts'),
    path('posts/create/', views.PostCreateView.as_view(), name='create_post'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail_post'),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='update_post'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
    path('likes/', views.LikeListView.as_view(), name='list_likes'),
    path('shares/', views.ShareListView.as_view(), name='list_shares'),
    path('comments/', views.CommentListView.as_view(), name='list_comments'),
    path('feed/user/', views.UserFeedView.as_view(), name='user_feed'),
    path('feed/persona/<int:persona_id>/', views.PersonaFeedView.as_view(), name='persona_feed'),
    path('feed/topic/<int:prompts_id>/', views.TopicFeedView.as_view(), name='topic_feed'),
]
