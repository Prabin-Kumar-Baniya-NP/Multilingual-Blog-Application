from django.urls import path
from comment import views
app_name = "Post"

urlpatterns = [
    path("get-comments/<int:postID>/<int:startIndex>", views.get_comments_ajax, name="get-comments"), 
    path("post-comment/", views.post_comment_ajax, name="post-comment"),
    path("delete-comment/<int:comment_id>/<int:post_id>", views.delete_comment, name = "delete-comment")    
]
