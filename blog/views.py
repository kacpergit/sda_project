from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import PostForm
from blog.models import Post

def hello_blog(request):
    return render(
        request,
        template_name='hello.html',
        context={'posts': Post.objects.all()}
    )


class PostView(generic.ListView):
    template_name = "hello.html"
    model = Post

class PostNew(generic.CreateView):
    template_name = "post_new.html"
    form_class = PostForm
    success_url = reverse_lazy('post_new')


class PostUpdate(generic.UpdateView):
    template_name = "post_new.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('index')
