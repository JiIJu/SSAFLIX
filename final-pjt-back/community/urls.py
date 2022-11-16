from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:review_pk>/like/', views.like, name='like'),
    path('<int:review_pk>/<int:comment_pk>/cocomments/create/', views.create_cocomment, name='create_cocomment'),
    path('<int:review_pk>/<int:comment_pk>/like/', views.comment_like, name='comment_like'),
    path('<int:review_pk>/<int:comment_pk>/<int:cocomment_pk>/cocomments_like/', views.cocomment_like, name='cocomment_like'),
]
