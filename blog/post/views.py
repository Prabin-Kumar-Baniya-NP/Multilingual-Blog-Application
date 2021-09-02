from django.core.paginator import Paginator
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from comment.models import Comment
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, View 
from post.models import Post
from category.models import Category
from post.forms import PostCreationForm, PostUpdationForm
from django.urls import reverse_lazy
from comment.forms import AddCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class PostCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """
    This view will handle creation of new post
    """
    model = Post
    form_class = PostCreationForm
    template_name = "post/create-post.html"
    success_url = reverse_lazy("post:manage-post")
    success_message = "%(title)s Post Created Successfully and Sent for Approval"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["requested_user_id"] = self.request.user.id
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.error, "Please Enter Valid Data")
        return super().form_invalid(form)

class DashboardView(ListView):
    """
    This view will handle the dashboard page content list viewing.
    """
    model = Post
    context_object_name = "posts"
    template_name = "post/dashboard.html"
    ordering = ['-last_updated']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(status = "A").order_by("id").values("id", "name")[:4]
        return context
    
    def get_queryset(self):
        return super().get_queryset().filter(status = "A")
    
class PostDetailView(DetailView):
    """
    This view will show the requested post
    """
    model = Post
    context_object_name = "post"
    template_name = "post/post.html"

    def get_object(self, **kwargs):
        return get_object_or_404(Post, slug = self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AddCommentForm(
            initial={
                'post': self.get_object().id,
                'commented_by': self.request.user.username
                }
            )
        if self.request.user.is_authenticated:
            context["user_comments"] = Comment.objects.filter(post = self.get_object().id, commented_by = self.request.user)
        return context
    

class ManagePostListView(LoginRequiredMixin, ListView):
    """
    This view will return the post owned by authenticated user
    """
    model = Post
    context_object_name = "posts"
    template_name = "post/manage-post-list.html"
    paginate_by = 10
    ordering = ["-published_on"]

    def get_queryset(self):
        return super().get_queryset().filter(author = self.request.user.id)

class PostUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    This view will update the post owned by authenticated user
    """
    model = Post
    form_class = PostUpdationForm
    template_name = "post/update-post.html"
    success_url = reverse_lazy("post:manage-post")
    success_message = "%(title)s Post Updated Successfully"

    def get_queryset(self):
        return super().get_queryset().filter(author = self.request.user)
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.error, "Please Enter Valid Data")
        return super().form_invalid(form)

class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """
    This view will delete the post owned by authenticated user
    """
    model = Post
    success_url = reverse_lazy("post:manage-post")

    def test_func(self):
        return self.get_object().author == self.request.user

class SearchPost(View):
    def get(self, request):
        try:
            posts = Post.objects.filter(title__icontains = request.GET["post-title"])
        except:
            return HttpResponseRedirect(reverse("post:dashboard"))
        finally:
            paginator = Paginator(posts, 25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, "post/search-post.html", {'page_obj': page_obj})
