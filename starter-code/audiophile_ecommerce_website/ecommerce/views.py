from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Category, Product, Cart, CartItem
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, CartItemSerializer
from rest_framework import generics

#Product
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDestroyView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#Category
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class  = CategorySerializer

class CategoryDestroyView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#Cart
class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartRetrieveView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartUpdateView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDestroyView(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

#CartItem
class CartItemListCreateView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemRetrieveView(generics.RetrieveAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemUpdateView(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
class CartItemDestroyView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

