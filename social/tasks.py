# social/tasks.py
import logging
from celery import shared_task
from .models import Post

logger = logging.getLogger(__name__)

@shared_task
def cache_post(post_id):
    try:
        post = Post.objects.get(id=post_id)
        # Add your caching logic here
        logger.info(f"Cached post with ID: {post_id}")
    except Post.DoesNotExist:
        logger.error(f"Post with ID {post_id} does not exist.")

@shared_task
def notify_users(post_id):
    try:
        post = Post.objects.get(id=post_id)
        # Add your notification logic here
        logger.info(f"Notified users about post with ID: {post_id}")
    except Post.DoesNotExist:
        logger.error(f"Post with ID {post_id} does not exist.")
