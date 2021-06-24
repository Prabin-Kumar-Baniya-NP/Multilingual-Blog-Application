from django.db import models
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView 
from post.models import Post
from post.forms import PostCreationForm
from django.urls import reverse_lazy

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = "post/create-post.html"
    success_url = reverse_lazy("post:create-post")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "post/blog.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "post/post.html"

