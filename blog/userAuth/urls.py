from django.urls import path
from userAuth import views

app_name = "userAuth"

urlpatterns = [
    path("signup/", views.CreateUser.as_view(), name = "signup"),
    path("login/", views.LoginView.as_view(), name = "login"),
    path("logout/", views.logout_view, name = "logout"),
    path("view-profile/", views.ViewProfile.as_view(), name="view-profile"),
    path("update-profile/<int:pk>/", views.UpdateProfileView.as_view(), name="update-profile"),
    path("change-password/", views.ChangePasswordView.as_view(), name="change-password"),
]
