from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('search-foods/', csrf_exempt(views.search_foods), name='search_foods'),
    path('list/', views.dashboard, name='dashboard'),
    path('list/<slug:category_slug>/', views.dashboard, name='list_by_category'),
    path('add_ingredient/<str:category_slug>/<str:food_slug>/', views.ingredient, name='ingredient'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('<slug:category_slug>/', views.foods, name='foods'),
    path('<slug:category_slug>/<slug:food_slug>/', views.detail, name='detail'),


]
