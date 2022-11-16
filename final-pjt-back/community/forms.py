from django import forms
from .models import Review, Comment, Cocomment


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['review', 'user','co_like_users']

class CocommentForm(forms.ModelForm):

    class Meta:
        model = Cocomment
        exclude = ['comment', 'user','coco_like_users']
