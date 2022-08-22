from django.shortcuts import render
from .models import Post
# Create your views here.


def post_list(request):
    object = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': object})


def post_details(request,id):
    object = Post.objects.get(id=id)
    return render(request, 'blog/post_details.html', {'post':object})
