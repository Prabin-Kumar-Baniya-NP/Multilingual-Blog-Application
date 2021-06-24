from django.shortcuts import render
from category.forms import CategoryCreationForm, CategoryUpdationForm
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
        'categories': Category.objects.all()
    }
    return render(request, "category/manage-category-list.html", context)

def delete_category(request, category_id):
    """
    This view will delete the requested category object
    """
    requested_category = Category.objects.get(id= category_id)
    requested_category.delete()
    return HttpResponseRedirect(reverse("category:manage-category"))

def update_category(request, category_id):
    """
    This view will update the requested category
    """
    requested_category = Category.objects.get(id = category_id)
    if (request.method == "POST"):
        form = CategoryUpdationForm(request.POST, instance=requested_category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("category:manage-category"))
        else:
            return HttpResponseRedirect(reverse("category:manage-category"))
    else:
        context = {
            'form': CategoryUpdationForm(instance = requested_category),
        }
        return render(request, "category/update-category.html", context)
