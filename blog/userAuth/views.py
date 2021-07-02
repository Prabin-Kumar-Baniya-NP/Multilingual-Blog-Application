from django.contrib.auth.forms import PasswordChangeForm
from django.http import request
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from userAuth.forms import SignUpForm, LoginForm, UpdateProfileForm, ChangePasswordForm
from django.views.generic.edit import CreateView, FormView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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


class ViewProfile(LoginRequiredMixin, TemplateView):
    """
    This is an template view for viewing user profile
    """
    template_name = "userAuth/profile.html"

@login_required
def logout_view(request):
    """
    This view will log out the current user
    """
    logout(request)
    return HttpResponseRedirect(reverse("post:dashboard"))

@login_required
def update_profile(request):
    """
    This view will handle the profile updation of currently logged user
    """
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("user:view-profile"))
        else:
            return HttpResponseRedirect(reverse("user:update-profile"))
    else:
        context = {
            'form': UpdateProfileForm(instance = request.user)
        }
        return render(request, "userAuth/update-profile.html", context)

@login_required
def change_password(request):
    """
    This view will handle the changing of password of currently logged user
    """
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            updated_user = form.save()
            update_session_auth_hash(request, updated_user)
            print("Form Valid")
            return HttpResponseRedirect(reverse("user:view-profile"))
        else:
            print("Form Invalid")
            return ChangePasswordForm(reverse("user:change-password"))
    else:
        context = {
            'form' : ChangePasswordForm(request.user)
        }
        return render(request, "userAuth/change-password.html", context)
