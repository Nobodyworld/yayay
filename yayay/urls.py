# yayay/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('accounts/', include('allauth.urls')),
    path('core/', include('core.urls')),
    path('artifacts/', include('artifacts.urls')),
    path('users/', include('users.urls')),
    path('collectives/', include('collectives.urls')),
    path('goals/', include('goals.urls')),
    path('problems/', include('problems.urls')),
    path('possessions/', include('possessions.urls')),
    path('personas/', include('personas.urls')),
    path('solutions/', include('solutions.urls')),
    path('content/', include('content.urls', namespace='content')),  # Ensure namespace is correct
    path('social/', include('social.urls')),
    path('prompts/', include('prompts.urls')),
    path('metrics/', include('metrics.urls')),
    path('leveling/', include('leveling.urls')),
    path('transactions/', include('transactions.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
