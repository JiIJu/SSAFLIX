from django.shortcuts import render , redirect
from django.views.decorators.http import require_safe
from .models import Movie , Genre
from .forms import MovieForm , GenreForm
# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request,'movies/index.html',context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # form = MovieForm(request)
    context = {
        'movie' : movie,
    }
    return render(request,'movies/detail.html',context)

@require_safe
def recommended(request):
    if request.user.is_authenticated:
        movies = Movie.objects.order_by('-popularity')
        movies = movies[0:10]
        context = {
            'movies' : movies,
        }
        return render(request,'movies/recommended.html',context)
    
    return redirect('accounts:login')