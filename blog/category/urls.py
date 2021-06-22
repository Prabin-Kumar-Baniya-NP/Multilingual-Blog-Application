from django.urls import path
from category import views

app_name = "Category"

urlpatterns = [
    path("create-category/", views.create_category, name="create-category"),
    path("manage-category/", views.manage_category, name="manage-category"),
]
