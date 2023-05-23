from rest_framework import serializers
from .models import Category, Products, CartItem, Cart

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug','image')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'image', 'description', 'price', 'category', 'slug')

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity', 'total_price', 'cart')   

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user','products','quantity', 'total_price',)  

