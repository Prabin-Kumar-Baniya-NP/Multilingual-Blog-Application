from django.urls import path
from post import views
app_name = "post"

urlpatterns = [
    path("create-post/", views.PostCreateView.as_view(), name="create-post"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("view-post/<int:pk>/", views.PostDetailView.as_view(), name="view-post"),
    path("manage-post/", views.ManagePostListView.as_view(), name="manage-post"),
    path("update-post/<int:pk>/", views.PostUpdateView.as_view(), name="update-post"),
    path("delete-post/<int:pk>/", views.PostDeleteView.as_view(), name="delete-post"),
]
