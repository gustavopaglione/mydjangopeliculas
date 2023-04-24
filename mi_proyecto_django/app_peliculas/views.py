from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie


def index(request):
    return render(request, 'index.html')

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'


from django.shortcuts import render
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movie_list.html', context)

def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'index.html', context)

def tu_vista(request):
    # Obtener el objeto de imagen desde el modelo
    imagen = TuModelo.objects.get(id=1).poster

    # Pasar la imagen a la plantilla
    context = {'imagen': imagen}
    return render(request, 'tu_plantilla.html', context)