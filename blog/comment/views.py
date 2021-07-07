from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from comment.models import Comment
from django.http import Http404
from django.core.paginator import Paginator
from comment.forms import AddCommentForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
import json
from django.contrib.auth.decorators import login_required


def get_comments_ajax(request, postID, pnum):
    """
    This view handles the get request for comment made using ajax method ONLY
    """
    if request.is_ajax():
        if request.user.is_authenticated:
            comments = Comment.objects.filter(
                post=postID).order_by("id").values(
                    "body", "commented_on", "updated_on", "likes", "dislikes",
                    "commented_by").exclude(commented_by=request.user)
        else:
            comments = Comment.objects.filter(
                post=postID).order_by("id").values("body", "commented_on",
                                                   "updated_on", "likes",
                                                   "dislikes", "commented_by")
        p = Paginator(comments, 4)
        if (pnum in p.page_range):
            page_num = p.page(pnum)
            comment_objects_list = list(page_num.object_list)
            return JsonResponse({"commentsData": comment_objects_list})
        else:
            return JsonResponse({})
    else:
        raise Http404("This type of get method is not allowed")


@login_required
def post_comment_ajax(request):
    """
    This view handles the post request for comment made using ajax method ONLY
    """
    if request.method == "POST" and request.is_ajax() == True:
        body_unicode = request.body.decode('utf-8')
        form_data = json.loads(body_unicode)
        new_comment = AddCommentForm(form_data)
        if new_comment.is_valid():
            new_comment.save()
            return JsonResponse({'status': 'success'})
        else:
            raise Http404("Invalid Data!")
    else:
        raise Http404("This type of method is not allowed")


@login_required
def delete_comment(request, comment_id, post_id):
    """
    This view will delete the comments made by authenticated user
    """
    if request.user.is_authenticated:
        requested_comment = get_object_or_404(Comment, id=comment_id)
        if requested_comment.commented_by == request.user:
            requested_comment.delete()
            return HttpResponseRedirect(
                reverse("post:view-post", kwargs={'pk': post_id}))
        else:
            raise Http404("You can only delete your comments")
