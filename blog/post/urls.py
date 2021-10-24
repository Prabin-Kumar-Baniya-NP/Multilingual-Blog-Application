from django.urls import path, include
from post import views
from rest_framework.routers import SimpleRouter


app_name = "post"

router = SimpleRouter()
router.register(r'', views.PostAPIViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("<int:postID>/comments/", views.get_comments_by_postID, name="get-comments-by-post")
]