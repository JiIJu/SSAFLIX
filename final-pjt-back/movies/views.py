from django.shortcuts import render , redirect
from django.views.decorators.http import require_safe
from .models import Movie , Genre

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import MovieForm , GenreForm
from .serializers import MovieSerializer , GenreSerializer
# Create your views here.
# @require_safe
@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        # context = {
        #     'movies' : movies,
        # }
        return Response(serializer.data,status=status.HTTP_200_OK)
        # return render(request,'movies/index.html',context)


# @require_safe
@api_view(['GET'])
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # form = MovieForm(request)
    context = {
        'movie' : movie,
    }
    return render(request,'movies/detail.html',context)

# @require_safe
@api_view(['GET'])
def recommended(request):
    if request.user.is_authenticated:
        movies = Movie.objects.order_by('-popularity')
        movies = movies[0:10]
        context = {
            'movies' : movies,
        }
        return render(request,'movies/recommended.html',context)
    
    return redirect('accounts:login')