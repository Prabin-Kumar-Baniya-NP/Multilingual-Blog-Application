from django.shortcuts import render
from category.forms import CategoryCreationForm
from category.models import Category
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def create_category(request):
    """
    This view will to handle the creation of category objects
    """
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        created_by = request.POST["created_by"]
        new_category = Category.objects.create(name = name, description = description, created_by = created_by)
        return HttpResponseRedirect(reverse("category:create-category"))
    else:
        context = {
            'form': CategoryCreationForm(),
        }
        return render(request, "category/create-category.html", context)

def manage_category(request):
    """
    This view will show all the categories which is created by the user
    """
    context = {
        
    }
    return render(request, "category/manage-category-list.html", context)