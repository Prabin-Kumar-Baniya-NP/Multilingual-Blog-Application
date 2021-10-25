from django.urls import path
from author import views

app_name = "author"

urlpatterns = [
    path("<int:pk>/category/", views.AuthorCategoryListView.as_view(), name="author-category"),
    path("<int:pk>/posts/", views.AuthorPostsListView.as_view(), name="author-posts")
]
