from .models import Cinema, Screening
from movielist.serializers import MovieSerializer
from rest_framework import serializers


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()

    class Meta:
        model = Cinema
        fields = ('id', 'name', 'city', 'movies')

    def get_movies(self, obj):
        movies = []
        for movie in obj.movies.all():
            movies.append({
                'title': movie.title,
                'director': movie.director.name,
            })
        return movies


class ScreeningSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()
    cinema = serializers.SerializerMethodField()

    class Meta:
        model = Screening
        fields = ('id', 'movie', 'cinema', 'date')

    def get_movie(self, obj):
        return obj.movie.title

    def get_cinema(self, obj):
        cinema = obj.cinema
        return {
            'name': cinema.name,
            'city': cinema.city,
        }
