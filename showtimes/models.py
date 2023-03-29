from django.db import models
from movielist.models import Movie
# Create your models here.


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie, through='Screening')

    def __str__(self):
        return self.name


class Screening(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_screening', on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, related_name='cinema_screening', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.movie
