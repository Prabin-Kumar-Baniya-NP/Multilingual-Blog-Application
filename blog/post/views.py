from django.db.models import query
from django.http import request
from comment.models import Comment
from django.db import models
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from post.models import Post
from category.models import Category
from post.forms import PostCreationForm, PostUpdationForm
from django.urls import reverse_lazy
from comment.forms import AddCommentForm

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
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class DashboardView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "post/blog.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Post.objects.filter().order_by("id")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().order_by("id").values("id", "name")[:4]
        return context
    
class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "post/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AddCommentForm(
            initial={
                'post': self.kwargs['pk'],
                'commented_by': self.request.user
                }
            )
        if self.request.user.is_authenticated:
            context["user_comments"] = Comment.objects.filter(commented_by = self.request.user)
        return context
    

class ManagePostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "post/manage-post-list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Post.objects.filter().order_by("id")
        return queryset
    

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdationForm
    template_name = "post/update-post.html"
    success_url = reverse_lazy("post:manage-post")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("post:manage-post")
    
