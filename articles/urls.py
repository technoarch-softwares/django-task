from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views
from django.views.static import serve
from django.conf import settings

from news.api import HomeViewSet


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    # Home Url
    url(r'^$', 'news.views.home', name='home'),
    url(r'^load_more_news/$', 'news.views.load_more_news', name='load_more_news'),

    # Home API url
    url(r'^api/$', HomeViewSet.as_view(), name='home'),

    # Media Url
    url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT})
]
