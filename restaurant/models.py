from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='images/category/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Food(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category,
                                 related_name='foods',
                                 on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/food/', blank=True)

    def get_absolute_url_admin(self):
        return reverse('restaurant:ingredient', args=[self.category.slug, self.slug])

    def get_absolute_url(self):
        return reverse('restaurant:detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, default='')
    weight = models.CharField(max_length=100)
    food = models.ForeignKey(Food,
                             related_name='ingredients',
                             on_delete=models.CASCADE)

    def __str__(self):
        return f"Ingredient for {self.food.name}."
