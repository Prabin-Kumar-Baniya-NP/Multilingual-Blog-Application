from django.db import models
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from post.models import Post
from category.models import Category
from post.forms import PostCreationForm, PostUpdationForm
from django.urls import reverse_lazy

class PostCreateView(CreateView):
    """
    This view will handle creation of +
    """
    model = Post
    form_class = PostCreationForm
    template_name = "post/create-post.html"
    success_url = reverse_lazy("post:create-post")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class DashboardView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "post/blog.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().order_by("id").values("id", "name")[:4]
        return context
    
class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "post/post.html"

class ManagePostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "post/manage-post-list.html"
    paginate_by = 5

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdationForm
    template_name = "post/update-post.html"
    success_url = reverse_lazy("post:manage-post")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("post:manage-post")
    
