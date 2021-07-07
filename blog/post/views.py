from comment.models import Comment
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from post.models import Post
from category.models import Category
from post.forms import PostCreationForm, PostUpdationForm
from django.urls import reverse_lazy
from comment.forms import AddCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    This view will handle creation of new post
    """
    model = Post
    form_class = PostCreationForm
    template_name = "post/create-post.html"
    success_url = reverse_lazy("post:manage-post")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["requested_user_id"] = self.request.user.id
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class DashboardView(ListView):
    """
    This view will handle the dashboard page content list viewing.
    """
    model = Post
    context_object_name = "posts"
    template_name = "post/blog.html"
    paginate_by = 5
    ordering = ['-last_updated']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().order_by("id").values("id", "name")[:4]
        return context
    
class PostDetailView(DetailView):
    """
    This view will show the requested post
    """
    model = Post
    context_object_name = "post"
    template_name = "post/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AddCommentForm(
            initial={
                'post': self.kwargs['pk'],
                'commented_by': self.request.user.username
                }
            )
        if self.request.user.is_authenticated:
            context["user_comments"] = Comment.objects.filter(commented_by = self.request.user)
        return context
    

class ManagePostListView(LoginRequiredMixin, ListView):
    """
    This view will return the post owned by authenticated user
    """
    model = Post
    context_object_name = "posts"
    template_name = "post/manage-post-list.html"
    paginate_by = 5
    ordering = ["-published_on"]


    def get_queryset(self):
        queryset = super(ManagePostListView, self).get_queryset()
        queryset = queryset.filter(author = self.request.user.id)
        return queryset

class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    This view will update the post owned by authenticated user
    """
    model = Post
    form_class = PostUpdationForm
    template_name = "post/update-post.html"
    success_url = reverse_lazy("post:manage-post")

    def get_queryset(self):
        return super().get_queryset().filter(author = self.request.user)
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """
    This view will delete the post owned by authenticated user
    """
    model = Post
    success_url = reverse_lazy("post:manage-post")

    def test_func(self):
        return self.get_object().author == self.request.user
    
