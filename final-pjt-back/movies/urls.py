# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('movies/', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended/', views.recommended, name='recommended'),
    # # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # # optional UI
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
