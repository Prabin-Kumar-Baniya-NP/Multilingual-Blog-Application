from django.urls import path, include
from rest_framework import views
from category import views


app_name = "Category"


urlpatterns = [
    path("", views.get_create_category, name="get-create-category"),
    path("<int:pk>/", views.get_update_delete_category, name="update-delete-category"),
    path("author/<int:userID>/", views.author_category_list, name="author-category-detail"),
]