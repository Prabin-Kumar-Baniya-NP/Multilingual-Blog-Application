from django.contrib.auth.models import User
from django.shortcuts import render
from category.forms import CategoryCreationForm, CategoryUpdationForm
from category.models import Category
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from post.models import Post

@login_required
def create_category(request):
    """
    This view will to handle the creation of category objects
    """
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        created_by_id = request.POST["created_by"]
        created_by_user_model = User.objects.get(id = created_by_id)
        new_category = Category.objects.create(name = name, description = description, created_by = created_by_user_model)
        return HttpResponseRedirect(reverse("category:manage-category"))
    else:
        context = {
            'form': CategoryCreationForm(request.user.id),
        }
        return render(request, "category/create-category.html", context)

@login_required
def manage_category(request):
    """
    This view will show all the categories which is created by the user
    """
    categories = Category.objects.filter(created_by = request.user.id)
    paginator = Paginator(categories, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'category/manage-category-list.html', {'page_obj': page_obj})

@login_required
def delete_category(request, category_id):
    """
    This view will delete the requested category object
    """
    requested_category = Category.objects.get(id= category_id)
    if requested_category.created_by == request.user:
        requested_category.delete()
        return HttpResponseRedirect(reverse("category:manage-category"))
    else:
        return HttpResponseRedirect(reverse("category:manage-category"))
    

@login_required
def update_category(request, category_id):
    """
    This view will update the requested category
    """
    requested_category = Category.objects.get(id = category_id)
    if requested_category.created_by == request.user:
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
    else:
        return HttpResponseRedirect(reverse("category:manage-category"))
    

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

def get_posts_by_category(request, categoryID):
    post_list = Post.objects.filter(category = categoryID).order_by("-published_on")
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "category/category-post.html", {"page_obj": page_obj})