from django.shortcuts import render , redirect
from django.views.decorators.http import require_safe
from .models import Movie , Genre

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated

from .forms import MovieForm , GenreForm
from .serializers import MovieSerializer , GenreSerializer , MovieListSerializer
# Create your views here.
# @require_safe
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies,many=True)
        # context = {
        #     'movies' : movies,
        # }
        return Response(serializer.data,status=status.HTTP_200_OK)
        # return render(request,'movies/index.html',context)


# @require_safe
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # form = MovieForm(request)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    # context = {
    #     'movie' : movie,
    # }
    # return render(request,'movies/detail.html',context)

# @require_safe
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommended(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            movies = Movie.objects.order_by('-popularity')
            movies = movies[0:10]
            serializer = MovieSerializer(movies,many=True)
            return Response(serializer.data)
            # context = {
            #     'movies' : movies,
            # }
            # return render(request,'movies/recommended.html',context)
    
    return redirect('accounts:login')