from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Review, Comment, Cocomment
from .forms import ReviewForm, CommentForm, CocommentForm
from django.http import JsonResponse

@require_GET
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST) 
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_GET
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    cocomment_form = CocommentForm()
    # cocomments = Comment.cocomment_set.all()
    context = {
        'review': review,
        'comment_form': comment_form,
        'cocomment_form' : cocomment_form,
        'comments': comments,
        # 'cocomments' : cocomments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)


@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            isLiked = False
        else:
            review.like_users.add(user)
            isLiked = True
        context = {
            'isLiked' : isLiked,
            'isLikedCount' : review.like_users.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:login')


@require_POST
def create_cocomment(request,  review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    cocomment_form = CocommentForm(request.POST)
    if cocomment_form.is_valid():
        cocomment = cocomment_form.save(commit=False)
        cocomment.comment = comment
        cocomment.user = request.user
        cocomment.save()
        return redirect('community:detail',review_pk)
    context = {
        'cocomment_form': cocomment_form,
        'comment': comment,
        'cocomments': comment.cocomment_set.all(),
    }
    return render(request, 'community/detail.html', context)


@require_POST
def comment_like(request, review_pk, comment_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        comment = get_object_or_404(Comment, pk=comment_pk)
        user = request.user

        if comment.co_like_users.filter(pk=user.pk).exists():
            comment.co_like_users.remove(user)
        else:
            comment.co_like_users.add(user)
        return redirect('community:detail',review_pk)
    return redirect('accounts:login')


@require_POST
def cocomment_like(request, review_pk, comment_pk, cocomment_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        cocomment = get_object_or_404(Cocomment, pk=cocomment_pk)
        user = request.user

        if cocomment.coco_like_users.filter(pk=user.pk).exists():
            cocomment.coco_like_users.remove(user)
        else:
            cocomment.coco_like_users.add(user)
        return redirect('community:detail',review_pk)
    return redirect('accounts:login')