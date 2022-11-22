from django.shortcuts import get_object_or_404


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Movie
from .serializers import MovieSerializer

# user 모델 가져오기
from django.contrib.auth import get_user_model

# Create your views here.
# 인기순으로 영화 제목 보내기 (selectBox)
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def home(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-popularity')[:1000]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 영화 상세 데이터
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


def random(request):
    pass



def genres(request):
    pass


def recommend(request):
    pass