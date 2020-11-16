from django.shortcuts import render
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML

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
                comment_author=form.cleaned_data["comment_author"],
                comment_body=form.cleaned_data["comment_body"],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    # print(comments)
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
    # print(logo)
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


def html_to_pdf_view(request, *args):
    """ some querys to help: prc = Post.objects.filter(comment__comment_body__isnull=False) hakee kaikki
    postaukset, joille on kommentti. miten sitten yhdistää Post ja Comment queryt yhdeksi? (ala pr | prc)"""
    # prc = Comment.objects.filter(comment_body__isnull=False)
    # pr = Post.objects.filter(*args).order_by('julkaistu_pvm')
    paragraphs = Post.objects.filter(*args).order_by('julkaistu_pvm')
    # paragraphs_b = Post.objects.select_related(*args).order_by('julkaistu_pvm')
    # paragraphs_c = Comment.objects.select_related(*args).order_by('comment_created_on')
    # paragraphs = {
    #     'paragraphs_b': paragraphs_b,
    #     'paragraphs_c': paragraphs_c
    # }
    html_string = render_to_string('pdf_template.html', {'paragraphs': paragraphs})

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/eKirja.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('eKirja.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="eKirja.pdf"'
        return response

    return response
