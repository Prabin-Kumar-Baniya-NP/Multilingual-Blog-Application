from django.shortcuts import render
from category.forms import CategoryCreationForm, CategoryUpdationForm
from category.models import Category
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.core.paginator import Paginator

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
    categories = Category.objects.all()
    paginator = Paginator(categories, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'category/manage-category-list.html', {'page_obj': page_obj})

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

def get_categories(request, pnum):
    if request.is_ajax():
        categories  = Category.objects.filter().order_by("id").values("id", "name")
        p = Paginator(categories, 4)
        if (pnum in p.page_range):
            page_num = p.page(pnum)
            category_objects_list = list(page_num.object_list)
            return JsonResponse(category_objects_list, safe=False)
        else:
            return JsonResponse({}, safe=False)
    else:
        raise Http404("This type of get method is not allowed")