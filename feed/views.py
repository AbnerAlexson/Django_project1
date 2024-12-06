from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

class HomePage(ListView): # this class is to render a template with all the post 
    http_method_names = ["get"] # users on the homepage can only GET posts and not modify them
    template_name = 'feed/homepage.html'
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:30] # homepage shows earliest 40 posts

class PostDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "feed/detail.html"
    model = Post
    context_object_name = "post"

class CreateNewPost(CreateView):
    model = Post
    template_name = "feed/create.html"
    fields = ['text']