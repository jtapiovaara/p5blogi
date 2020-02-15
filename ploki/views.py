from django.views import generic
from django.shortcuts import render


from .forms import CommentForm
from ploki.models import Post, Comment
from .filters import SuodataPosti


def ploki_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, 'ploki_index.html', context)

# class ploki_index(generic.ListView):
#     model = Post
#     template_name = 'ploki_index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = SuodataPosti(self.request.GET, queryset=self.get_queryset())
#         return context


def ploki_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'ploki_category.html', context)


def ploki_detail(request, pk):
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


# def ploki_etsi(request):
#     template = 'ploki_etsi.html'
#     query = request.GET.get('q')
#     # posts = Post.objects.filter(Q(title__contains=query) | Q(body__contains=query))
#     posts = Post.objects.filter(Q(title__contains=query))
#     context = {
#         'posts': posts,
#     }
#     return render(request, template, context)

# def ploki_etsi(request, search):
#     posts = Post.objects.filter(
#         title__name__contains=search
#     ).order_by(
#         '-created_on'
#     )
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'ploki_etsi.html', context)

# def ploki_index(request):
#     posts = Post.objects.all().order_by('-created_on')
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'ploki_index.html', context)


