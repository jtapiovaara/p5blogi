from django.shortcuts import render
from django.views.generic.dates import MonthArchiveView
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse


from .forms import CommentForm
from ploki.models import Post, Comment, Play, Category


def ploki_latest(request):
    template = 'ploki_detail.html'
    post = Post.objects.latest('julkaistu_pvm')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    # print(post.kuvitusta)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, template, context)


def ploki_detail(request, pk):
    # pk = 47
    template = 'ploki_detail.html'
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, template, context)


def ploki_index(request):
    posts = Post.objects.all().order_by('-created_on')
    logos = Category.objects.all()
    total = posts.count()
    context = {
        'logos': logos,
        'total': total,
        'posts': posts,
    }
    return render(request, 'ploki_index.html', context)


def ploki_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    logo = Category.objects.get(name=category)
    print(logo.kuva)
    context = {
        'logo': logo,
        'category': category,
        'posts': posts
    }
    return render(request, 'ploki_category.html', context)


def graph(request):
    return render(request, 'graph/graph.html')


def play_count_by_month(request):
    data = Play.objects.all() \
        .extra(
            select={
                'month': connections[Play.objects.db].ops.date_trunc_sql('month', 'date')
            }
        ) \
        .values('month') \
        .annotate(count_items=Count('id'))
    return JsonResponse(list(data), safe=False)


