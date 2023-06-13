from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about-us/', views.about_us, name='about_us'),
    path('articles/', views.articles, name='articles'),
    path('contact-us/', views.contact, name='contact'),
    path('sitemap/', views.sitemap, name='sitemap'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)