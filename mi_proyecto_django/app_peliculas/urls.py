from django.urls import re_path
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('about-us/', views.about_us, name='about-us'),
    path('articles/', views.articles, name='articles'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('sitemap/', views.sitemap, name='sitemap'),
     path('', views.movie_list, name='movie_list'),


    re_path(r'^movies/$', views.MovieListView.as_view(), name='movie_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

