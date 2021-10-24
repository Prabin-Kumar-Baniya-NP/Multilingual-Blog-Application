from django.urls import path
from comment import views

app_name = "comment"

urlpatterns = [
    path("", views.CommentsCreateAPIView.as_view(), name="create-comment"),
    path("<int:pk>/", views.CommentsModifyAPIView.as_view(), name="modify-comments"),
]
