from django.urls import path
from post import views


app_name = "Post"

urlpatterns = [
    path("create-post/", views.PostCreateView.as_view(), name="create-post"),
    path("get-post/", views.PostListView.as_view(), name="get-all-post"),
    path("get-post/<int:pk>/", views.PostRetrieveView.as_view(), name="get-post-instance"),
    path("update-post/<int:pk>/", views.PostUpdateView.as_view(), name="update-post"),
    path("delete-post/<int:pk>/", views.PostDeleteView.as_view(), name="delete-post"),
]
