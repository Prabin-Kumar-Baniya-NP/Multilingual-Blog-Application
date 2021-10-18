from category.serializers import CategorySerializer
from category.models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def get_create_category(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT", "DELETE"])
def update_delete_category(request, pk):
    try:
        category = Category.objects.get(id = pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        if category.created_by == request.user.id:
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
    elif request.method == "DELETE":
        if category.created_by == request.user.id:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

