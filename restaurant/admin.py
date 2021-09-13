from django.contrib import admin

from .models import Category, Food, Ingredient


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', ]
    list_filter = ['category']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', ]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_filter = ['food']
    list_display = ['food', 'name', 'weight']
