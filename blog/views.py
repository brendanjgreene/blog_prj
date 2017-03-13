from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


def new_post(request):
    form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})


def get_base(request):
    return render(request, "base.html")


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def top_lists(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-views')[:5]
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, id):
    """
    Create a view that returns a single
    Post object based on the post ID and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is not found
    """
    post = get_object_or_404(Post, pk=id)
    post.views += 1  #adds a view to the view counter
    post.save()
    return render(request, "postdetail.html", {'post': post})


