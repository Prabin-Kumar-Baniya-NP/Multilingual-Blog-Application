from django.db.models import fields
from django.http.response import HttpResponse, HttpResponseRedirect
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
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q

def get_comments_ajax(request, postID, startIndex):
    """
    This view handles the get request for comment made using ajax method ONLY
    """
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if is_ajax:
        if request.user.is_authenticated:
            comments = Comment.objects.filter(post=postID).filter(~Q(commented_by=request.user.username)).order_by("id")[startIndex:startIndex+4]
        else:
            comments = Comment.objects.filter(post=postID).order_by("id")[startIndex: startIndex+4]
        json_comments = serialize('json', comments, cls=DjangoJSONEncoder, fields = ["body", "commented_by"])
        return HttpResponse(json_comments)
    else:
        raise Http404("This type of get method is not allowed")


@login_required
def post_comment_ajax(request):
    """
    This view handles the post request for comment made using ajax method ONLY
    """
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if request.method == "POST" and is_ajax == True:
        try:
            form_data = json.loads(request.body)
            new_comment = AddCommentForm(form_data)
            if new_comment.is_valid():
                new_comment.save()
                return JsonResponse({"status": "success"})
            else:
                raise Http404("Invalid Data!")
        except Exception as e:
            raise Http404("Something went wrong!")
    else:
        raise Http404("This type of method is not allowed")


@login_required
def delete_comment(request, comment_id, post_id):
    """
    This view will delete the comments made by authenticated user
    """
    if request.user.is_authenticated:
        requested_comment = get_object_or_404(Comment, id=comment_id)
        if requested_comment.commented_by == request.user.username:
            requested_comment.delete()
            return HttpResponseRedirect(
                reverse("post:view-post", kwargs={'slug': requested_comment.post.slug}))
        else:
            raise Http404("You can only delete your comments")
