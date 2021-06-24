from django.urls import path
from post import views
app_name = "post"

urlpatterns = [
    path("create-post/", views.PostCreateView.as_view(), name="create-post"),
    path("blog-dashboard/", views.PostListView.as_view(), name="blog-dashboard"),
    path("view-post/<int:pk>", views.PostDetailView.as_view(), name="view-post"),
]
