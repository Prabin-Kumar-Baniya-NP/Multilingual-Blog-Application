from django.shortcuts import render
from django.http import JsonResponse
from comment.models import Comment
from django.http import Http404
from django.core.paginator import Paginator

def get_comments_ajax(request, postID, pnum):
    if request.is_ajax():
        comments = Comment.objects.filter(post = postID).order_by("id").values(
            "body",
            "commented_on",
            "updated_on",
            "likes",
            "dislikes",
            "commented_by"
        )
        p = Paginator(comments, 4)
        if (pnum in p.page_range):
            page_num = p.page(pnum)
            comment_objects_list = list(page_num.object_list)
            return JsonResponse(comment_objects_list, safe=False)
        else:
            return JsonResponse({}, safe=False)
    else:
        raise Http404("This type of get method is not allowed")