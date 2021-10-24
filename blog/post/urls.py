from django.urls import path, include
from post import views
from rest_framework.routers import SimpleRouter


app_name = "post"

router = SimpleRouter()
router.register(r'', views.PostAPIViewSet)

urlpatterns = router.urls