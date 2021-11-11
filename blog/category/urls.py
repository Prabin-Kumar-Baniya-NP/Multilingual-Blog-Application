from django.urls import path, include
from rest_framework import views
from category import views


app_name = "category"


urlpatterns = [
    path("", views.get_or_create_category, name="get-or-create-category"),
    path("<int:pk>/", views.get_update_delete_category, name="update-delete-category"),
    path("<int:categoryID>/posts/", views.get_post_by_category, name="get-posts-by-category"),
]