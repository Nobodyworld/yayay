# File: social\views.py
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, DetailView, RedirectView, DeleteView, UpdateView
from .models import Post, Category, Tag, Notification, Like, Share, Comment
from .forms import TagForm, CategoryForm, PostForm
from .tasks import cache_post, notify_users
from django.contrib.auth import get_user_model
from personas.models import Persona
from prompts.models import Prompts

User = get_user_model()

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class TagCreateView(AdminRequiredMixin, CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'app/social.html'
    success_url = reverse_lazy('social:tag_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'create_tag'
        return context

class CategoryCreateView(AdminRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'app/social.html'
    success_url = reverse_lazy('social:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'create_category'
        return context

class TagDetailView(DetailView):
    model = Tag
    template_name = 'app/social.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'detail_tag'
        return context

class TagListView(ListView):
    model = Tag
    template_name = 'app/social.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'list_tags'
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'app/social.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'detail_category'
        return context

class CategoryListView(ListView):
    model = Category
    template_name = 'app/social.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'list_categories'
        return context

class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'app/social.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'list_notifications'
        return context

class NotificationReadView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('social:list_notifications')

    def get_redirect_url(self, *args, **kwargs):
        notification = get_object_or_404(Notification, pk=kwargs['pk'], user=self.request.user)
        notification.is_read = True
        notification.save()
        return super().get_redirect_url(*args, **kwargs)

class NotificationDeleteView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('social:list_notifications')

    def get_redirect_url(self, *args, **kwargs):
        Notification.objects.filter(pk=kwargs['pk'], user=self.request.user).delete()
        return super().get_redirect_url(*args, **kwargs)

class FollowView(LoginRequiredMixin, View):
    def get(self, request, followed_user_id):
        followed_user = get_object_or_404(User, pk=followed_user_id)
        if request.user.is_following(followed_user):
            request.user.unfollow(followed_user)
        else:
            request.user.follow(followed_user)
        return redirect('social:profile', pk=followed_user_id)

class PostListView(ListView):
    model = Post
    template_name = 'app/social.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(is_active=True).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'list_posts'
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'app/social.html'
    success_url = reverse_lazy('social:list_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        cache_post.delay(form.instance.pk)
        notify_users.delay(form.instance.pk)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'create_post'
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'app/social.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'detail_post'
        return context

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'app/social.html'

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('social:detail_post', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'update_post'
        return context

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'app/social.html'
    success_url = reverse_lazy('social:list_posts')

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'delete_post'
        return context

class LikeListView(LoginRequiredMixin, ListView):
    model = Like
    template_name = 'app/social.html'
    context_object_name = 'likes'
    paginate_by = 10

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'list_likes'
        return context

class ShareListView(LoginRequiredMixin, ListView):
    model = Share
    template_name = 'app/social.html'
    context_object_name = 'shares'
    paginate_by = 10

    def get_queryset(self):
        return Share.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'list_shares'
        return context

class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'app/social.html'
    context_object_name = 'comments'
    paginate_by = 10

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'list_comments'
        return context

class BaseFeedView(LoginRequiredMixin, ListView):
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        raise NotImplementedError("Subclasses must implement get_queryset method")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_additional_context())
        return context

    def get_additional_context(self):
        return {}

class UserFeedView(BaseFeedView):
    template_name = 'app/social.html'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'user_feed'
        return context

class PersonaFeedView(BaseFeedView):
    template_name = 'app/social.html'

    def get_queryset(self):
        persona_id = self.kwargs.get('persona_id')
        return Post.objects.filter(persona_id=persona_id).order_by('-created_at')

    def get_additional_context(self):
        return {'persona': get_object_or_404(Persona, id=self.kwargs.get('persona_id'))}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'persona_feed'
        return context

class TopicFeedView(BaseFeedView):
    template_name = 'app/social.html'

    def get_queryset(self):
        prompts_id = self.kwargs.get('prompts_id')
        return Post.objects.filter(prompts_id=prompts_id). order_by('-created_at')

    def get_additional_context(self):
        return {'prompts': get_object_or_404(Prompts, id=self.kwargs.get('prompts_id'))}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'topic_feed'
        return context
