from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import json

from .forms import IngredientForm
from .models import Food, Ingredient, Category


def home(request):
    categories = Category.objects.all()
    return render(request, 'restaurant/index.html', {'categories': categories})


def foods(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    foods = Food.objects.filter(category=category)
    print(foods)
    return render(request, 'restaurant/food_list.html', {'category': category,
                                                         'foods': foods})


def detail(request, category_slug, food_slug):
    food = get_object_or_404(Food,
                             category__slug=category_slug,
                             slug=food_slug)
    previous = request.GET.get('previous')
    return render(request, 'restaurant/food_detail.html', {'food': food,
                                                           'previous': previous})


def search_foods(request):
    if request.method == 'POST':
        search_val = json.loads(request.body).get('searchText')
        category_slug = json.loads(request.body).get('category')
        foods = Food.objects.filter(category__slug=category_slug, name__icontains=search_val)
        data = foods.values()
        for i in data:
            food = Food.objects.get(id=i.get('id'))
            if food.image:
                i["image"] = food.image.url
            i["url"] = food.get_absolute_url()
        return JsonResponse(list(data), safe=False)


# Custom admin views
def dashboard(request, category_slug=None):
    if not request.user.is_staff:
        return redirect('restaurant:home')

    foods = Food.objects.all()
    categories = Category.objects.all()
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        foods = foods.filter(category=category)
    return render(request, 'restaurant/admin/dashboard.html', {'foods': foods,
                                                               'category': category,
                                                               'categories': categories})


def ingredient(request, category_slug, food_slug):
    if not request.user.is_staff:
        return redirect('restaurant:home')

    food = get_object_or_404(Food, category__slug=category_slug, slug=food_slug)
    print(food)
    if request.method == 'POST':
        form = IngredientForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.food = food
            new_form.save()
            messages.success(request, 'Ingredient added.')
            return redirect(food.get_absolute_url_admin())
    else:
        form = IngredientForm()

    return render(request, 'restaurant/admin/ingredient_form.html', {'form': form, 'food': food})


def delete(request, id):
    if not request.user.is_staff:
        return redirect('restaurant:home')

    ingredient = get_object_or_404(Ingredient, id=id)
    ingredient.delete()
    return redirect(request.GET.get('next'))
