from django.contrib import admin
from .models import Category, Notification, Follow, Tag, Post, Share, Like, Comment

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['message']

@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'object_id', 'created_at']
    search_fields = ['user__username', 'content_type']
    list_filter = ['created_at']
    ordering = ['-created_at']

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['user', 'follower', 'created_at']
    search_fields = ['user__username', 'follower__username']
    list_filter = ['created_at']
    ordering = ['-created_at']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'content', 'author__username']
    list_filter = ['author']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'object_id', 'created_at']
    search_fields = ['user__username', 'content_type']
    list_filter = ['created_at']
    ordering = ['-created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'object_id', 'created_at']
    search_fields = ['user__username', 'content_type']
    list_filter = ['created_at']
    ordering = ['-created_at']
