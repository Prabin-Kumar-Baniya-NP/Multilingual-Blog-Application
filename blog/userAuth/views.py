from django.http import request
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from userAuth.forms import SignUpForm, LoginForm, UpdateProfileForm, ChangePasswordForm
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

class CreateUser(CreateView):
    """
    This view will handle the creation of user
    """
    model = User
    form_class = SignUpForm
    template_name = "userAuth/signup.html"
    success_url = reverse_lazy("post:dashboard")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class LoginView(FormView):
    """
    This view will handle the login system of user
    """
    model = User
    form_class = LoginForm
    template_name = "userAuth/login.html"
    success_url = reverse_lazy("post:dashboard")

    def form_valid(self, form):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        user = authenticate(self.request, username = username, password = password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class ViewProfile(TemplateView):
    """
    This is an template view for viewing user profile
    """
    template_name = "userAuth/profile.html"

def logout_view(request):
    """
    This view will log out the current user
    """
    logout(request)
    return HttpResponseRedirect(reverse("post:dashboard"))

class UpdateProfileView(UpdateView):
    model = User
    form_class = UpdateProfileForm
    template_name = "userAuth/update-profile.html"
    success_url = reverse_lazy("user:view-profile")
    
    def form_valid(self, form):
        if self.request.POST["username"] == self.request.user.username:
            return super().form_valid(form)
        else:
            raise Http404("Permission Denied")
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class ChangePasswordView(FormView):
    model = User
    form_class = ChangePasswordForm
    template_name = "userAuth/reset-password.html"
    success_url = reverse_lazy("user:view-profile")
    
    def get_form_kwargs(self):
        return super().get_form_kwargs({'user': User.objects.get(id=self.request.user.id)})
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_valid(self, form):
        return super().form_valid(form)
