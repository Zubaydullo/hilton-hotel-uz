"""hotel_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings 
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns




urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('blog/', include('blog_post.urls')),
    path('manager/', include('hotel_manager.urls', namespace="hotel_manager")),
    path('accounts/', include('allauth.urls')), #google integration
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    urlpatterns += i18n_patterns(
    path('', include('user.urls')),
    path('blog/', include('blog_post.urls')),
    )


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
