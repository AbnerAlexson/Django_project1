from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class CreateNewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "feed/create.html"
    fields = ['text']
    success_url = '/'

    def dispatch(self, request, *args, **kwargs): # dispatch will run before form_valid()
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)  # this grabs the form, TODO turn to True when every is working as intended
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)