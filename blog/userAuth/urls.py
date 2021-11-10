from django.urls import path
from userAuth import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "userAuth"

urlpatterns = [
    path('token/get/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name="token-verify"),
    path("token/blacklist/", views.BlackListTokenView.as_view(), name="blacklist-token"),
    path("register/", views.RegisterUser.as_view(), name="register-user"),
    path("update-profile/<int:pk>/", views.UpdateUserProfileView.as_view(), name="update-profile"),
    path("change-password/", views.ChangePasswordView.as_view(), name="change-password"),
]
