from django.shortcuts import render
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})

def about_us(request):
    return render(request, 'index/about_us.html')

def about(request):
    return render(request, 'about.html')

def articles(request):
    return render(request, 'articles.html')

def contact(request):
    return render(request, 'contact-us.html')

def sitemap(request):
    return render(request, 'sitemap.html')