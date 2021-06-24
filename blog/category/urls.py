from django.urls import path
from django.urls import path
from category import views

app_name = "Category"

urlpatterns = [
    path("create-category/", views.create_category, name="create-category"),
    path("manage-category/", views.manage_category, name="manage-category"),
    path("delete-category/<int:category_id>", views.delete_category, name="delete-category"),
    path("update-category/<int:category_id>", views.update_category, name="update-category"),
]
