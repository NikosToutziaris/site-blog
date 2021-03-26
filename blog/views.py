# from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.db.models import Q


# Create your views here.

def post__list(request):
    cat = request.GET.get('cat', '')
    txt = request.GET.get('txt', '')
    try:
        cat = int(cat)
    except:
        cat = False
    if not cat:  # cat == False
        if txt == '':
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        else:
            posts = Post.objects.filter(published_date__lte=timezone.now()).filter(text__contains=txt).order_by(
                'published_date')
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).filter(category=cat).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_list(request):
    global posts
    cat = request.GET.get('cat', '')
    txt = request.GET.get('txt', '')
    try:
        cat = int(cat)
    except:
        cat = False

        if not cat:  # cat == False
            # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            posts = Post.objects.filter(
                (Q(text__contains=txt) | Q(title__contains=txt)) & Q(published_date__lte=timezone.now())).order_by(
                'published_date')
        else:
            # posts = Post.objects.filter(published_date__lte=timezone.now()).filter(category=cat). \
            #  order_by('published_date')
            posts = Post.objects.filter(
                (Q(text__contains=txt) | Q(title__contains=txt)) & Q(published_date__lte=timezone.now())).order_by(
                'published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})
