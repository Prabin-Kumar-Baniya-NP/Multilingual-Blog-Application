from django.urls import path
from userAuth import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "userAuth"

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name="token-verify"),
    path("signup/", views.CreateUser.as_view(), name = "signup"),
    path("login/", views.LoginView.as_view(), name = "login"),
    path("logout/", views.logout_view, name = "logout"),
    path("view-profile/", views.ViewProfile.as_view(), name="view-profile"),
    path("update-profile/", views.update_profile, name="update-profile"),
    path("change-password/", views.change_password, name="change-password"),
]
