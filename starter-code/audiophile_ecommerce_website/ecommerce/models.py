
from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique= True, blank=True)
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categoryImage = models.ImageField(upload_to ='product -images/')
    new = models.BooleanField(default=True)
    features = models.CharField(max_length=200, blank=True)
    includes = models.JSONField(default=list)

    def __str__(self):
         return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    categoryImage = models.ImageField(upload_to='category -images/')

    def __str__(self):
        return self.name


class Cart(models.Model):
        products = models.CharField(max_length=100, blank=True)
        quantity = models.IntegerField()
        price = models.DecimalField(max_digits=10, decimal_places=2)
        total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
        price_per_unit = 10

        def calculate_total_price(quantity, price):
            return quantity * price


class CartItem(models.Model):
    products = models.CharField(max_length=100, blank=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

