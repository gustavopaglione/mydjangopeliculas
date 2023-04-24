from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, help_text="Pon el nombre de genero")

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(help_text="Colocar el resumen de la pelicula")
    release_date = models.DateField()
    poster = models.ImageField(upload_to='posters/')
    rating = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
    

    @staticmethod
    def get_movies_by_genre(genre_name):
        movies = Movie.objects.filter(genres__name__icontains=genre_name)
        return movies

    @staticmethod
    def get_movies_by_director(director_name):
        movies = Movie.objects.filter(director__name__icontains=director_name)
        return movies
