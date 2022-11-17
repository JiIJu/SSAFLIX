from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    users_pick = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movies_picked')
    movie_id = models.CharField(max_length=100)
    title  = models.CharField(max_length=100)
    overview = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='movies')
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500)
    popularity = models.IntegerField()
    release_date = models.CharField(max_length=100)
    vote_avg = models.IntegerField()
    vote_cnt = models.IntegerField()

# class Movie(models.Model):
#     users_pick = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movies_picked')
#     movie_id = models.CharField(max_length=100)
#     title  = models.CharField(max_length=100)
#     overview = models.TextField()
#     # genre  = models.CharField(max_length=50)
#     genre = models.ManyToManyField(Genre)
#     poster_path = models.CharField(max_length=500)
#     backdrop_path = models.CharField(max_length=500)
#     popularity = models.IntegerField()
#     release_date = models.CharField(max_length=100)
#     vote_avg = models.IntegerField()
#     vote_cnt = models.IntegerField()

    # @classmethod
    # def initialize(cls):
    #     import requests
    #     API_KEY = '5b7913e29ceb285a780369f75e83d42e'
    #     for i in range(1, 11):
    #         URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&region=KR&language=ko-KR&page={i}'
    #         res = requests.get(URL).json()
    #         results = res['results']
    #         for result in results:
    #             cls.objects.create(
    #                 tmdb_id = result['id'], 
    #                 title = result['title'], 
    #                 overview = result['overview'], 
    #                 genre = result['genre_ids'], 
    #                 poster_path = 'https://www.themoviedb.org/t/p/original' + result['poster_path'], 
    #                 release_date = result['release_date'], 
    #                 vote_avg = result['vote_average'], 
    #                 vote_cnt = result['vote_count']
    #             )

'''
from movies.models import Movie
Movie.initialize()
'''