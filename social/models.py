from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Social(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        app_label = 'social'

class Follow(Social):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following', help_text=_("The user who is following"))

    def __str__(self):
        return f"{self.follower.username} follows {self.user.username}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Follow')
        verbose_name_plural = _('Follows')
        app_label = 'social'

class Like(Social):
    def __str__(self):
        return f"{self.user.username} likes {self.content_object}"

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')
        app_label = 'social'

class Share(Social):
    def __str__(self):
        return f"{self.user.username} shared {self.content_object}"

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')
        verbose_name = _('Share')
        verbose_name_plural = _('Shares')
        app_label = 'social'

class Configuration(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()

    def __str__(self):
        return f"{self.key}: {self.value}"

    @classmethod
    def get_value(cls, key):
        config = cls.objects.filter(key=key).first()
        return config.value if config else None

    class Meta:
        app_label = 'social'

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='categories', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = _("Categories")
        app_label = 'social'

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = _("Tags")
        app_label = 'social'

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        app_label = 'social'

class Post(models.Model):
    title = models.CharField(max_length=255, help_text=_("Title of the post"))
    content = models.TextField(help_text=_("Content of the post"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts', help_text=_("The user who created the post"))
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text=_("The date and time the post was created"))
    updated_at = models.DateTimeField(auto_now=True, help_text=_("The date and time the post was last updated"))
    is_active = models.BooleanField(default=True, help_text=_("Is the post currently active"))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('social:post_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        app_label = 'social'

class Comment(Social):
    text = models.TextField(help_text=_("The content of the comment"))

    def __str__(self):
        return f"Comment by {self.user.username} on {self.content_object}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        app_label = 'social'

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='posts/images/', help_text=_("Image of the post"))

    def __str__(self):
        return f"Image for post {self.post.title}"

    class Meta:
        verbose_name = _('Post Image')
        verbose_name_plural = _('Post Images')
        app_label = 'social'
