from django.urls import path, include
from rest_framework import views
from category import views

urlpatterns = [
    path("", views.get_create_category, name="get-create-category"),
    path("<int:pk>/", views.update_delete_category, name="update-delete-category"),
]