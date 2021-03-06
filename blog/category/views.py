from category.serializers import CategorySerializer
from category.models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import PageNumberPagination
from post.models import Post
from post.serializers import PostSerializer

@api_view(["GET", "POST"])
def get_or_create_category(request):
    """
    Returns approved category
    Adds a new category
    """
    if request.method == "GET":
        categories = Category.objects.filter(status="A").order_by("-created_on")
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(categories, request)
        serializer = CategorySerializer(result_page, many = True)
        return paginator.get_paginated_response(serializer.data)
    
    elif request.method == "POST":
        if request.user.is_authenticated:
            serializer = CategorySerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(["GET","PUT", "DELETE"])
def get_update_delete_category(request, pk):
    """
    GET: Returns instance of approved Category
    PUT: Updates the category instance
    Delete: Deletes the category instance
    """
    try:
        category = Category.objects.get(id = pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serializer = CategorySerializer(category)
        if serializer.data["status"] != 'A' and serializer.data["created_by"] != request.user.id:
            raise PermissionDenied(detail="Category is not Approved")
        return Response(serializer.data)
    
    elif request.method == "PUT":
        if request.user.is_authenticated:
            if category.created_by.id == request.user.id:
                serializer = CategorySerializer(category, data=request.data, context={"request": request})
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    elif request.method == "DELETE":
        if request.user.is_authenticated:
            if category.created_by.id == request.user.id:
                category.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(["GET"])
def get_post_by_category(request, categoryID):
    """
    Returns the posts based on category id
    """
    posts = Post.objects.filter(category = categoryID, status="A").order_by("-published_on")
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(posts, request)
    serializer = PostSerializer(result_page, many = True)
    return paginator.get_paginated_response(serializer.data)
