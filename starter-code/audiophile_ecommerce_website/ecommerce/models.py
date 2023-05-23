from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    # image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Products, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)


    def __str__(self):
        return f"Cart for {self.user.username}"

    # def __str__(self):
    #     return f"Cart #{self.id}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"CartItem #{self.id}"

    