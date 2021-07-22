from django.urls import path
from django.urls import path
from category import views

app_name = "category"

urlpatterns = [
    path("create-category/", views.create_category, name="create-category"),
    path("manage-category/", views.manage_category, name="manage-category"),
    path("delete-category/<int:category_id>", views.delete_category, name="delete-category"),
    path("update-category/<int:category_id>", views.update_category, name="update-category"),
    path("get-categories/<int:pnum>", views.get_categories, name="get-categories"),
    path("category-posts/<str:category_name>", views.get_posts_by_category, name = "category-posts"),
]
