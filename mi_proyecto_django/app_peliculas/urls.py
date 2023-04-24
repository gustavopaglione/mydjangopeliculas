from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.index, name='index'),

    re_path(r'^movies/$', views.MovieListView.as_view(), name='movie_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)