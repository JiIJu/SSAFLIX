from rest_framework import serializers
from .models import Movie , Genre
from accounts.serializers import UserSerializer

class MovieListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Movie
        # fields = ('title','release_date','popularity','vote_count','vote_average','overview','poster_path','genre')
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model : Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)
    # genre = GenreSerializer(many=True,read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('user',)