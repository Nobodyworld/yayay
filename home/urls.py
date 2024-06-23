# home/urls.py
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('index/', views.index_view, name='index'),
    path('content-home/', views.content_home, name='content_home'),  # Add this line
    path('landing/', views.LandingPageView.as_view(), name='landing_page'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('pricing/', views.PricingView.as_view(), name='pricing'),
    path('privacy/', views.PrivacyView.as_view(), name='privacy'),
    path('support/', views.SupportView.as_view(), name='support'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('feeds/', views.FeedListView.as_view(), name='feeds'),
    path('filter-feeds/', views.filter_feeds, name='filter_feeds'),
    path('feed/', views.FeedListView.as_view(), name='feed'),
]
