from django.core import paginator
from category.serializers import CategorySerializer
from category.models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import PageNumberPagination

@api_view(["GET", "POST"])
def get_create_category(request):
    if request.method == "GET":
        categories = Category.objects.filter(status="A")
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
def author_category_list(request, userID):
    if request.user.id == userID:
        categories = Category.objects.filter(created_by=userID)
    else:
        categories = Category.objects.filter(created_by=userID, status="A")
    if request.method == "GET":
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(categories, request)
        serializer = CategorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)