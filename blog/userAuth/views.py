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
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class CreateUser(SuccessMessageMixin, CreateView):
    """
    This view will handle the creation of user
    """
    model = User
    form_class = SignUpForm
    template_name = "userAuth/signup.html"
    success_url = reverse_lazy("post:dashboard")
    success_message = "%(username)s user created successfully"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Invalid Data Submitted ! Please Enter Valid Data")
        return super().form_invalid(form)

class LoginView(SuccessMessageMixin, FormView):
    """
    This view will handle the login system of user
    """
    model = User
    form_class = LoginForm
    template_name = "userAuth/login.html"
    success_url = reverse_lazy("post:dashboard")
    success_message = "Logged In Successfully"

    def form_valid(self, form):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        user = authenticate(self.request, username = username, password = password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.add_message(self.request, messages.ERROR, "User does not exist in the database")
            return HttpResponseRedirect(reverse("user:login"))
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please enter correct username and password")
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
    messages.success(request, "Logged out Successfully")
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
            messages.success(request, "Profile Updated Successfully")
            return HttpResponseRedirect(reverse("user:view-profile"))
        else:
            messages.error(request, "Invalid Data Submitted ! Please Enter Valid Data")
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
                messages.success(request, "Password Changed Successfully")
                return HttpResponseRedirect(reverse("user:view-profile"))
        else:
            messages.error(request, "Unable to change password ! Please Enter Valid Password")
            return HttpResponseRedirect(reverse("user:change-password"))
    else:
        context = {
            'form' : ChangePasswordForm(request.user)
        }
        return render(request, "userAuth/change-password.html", context)
