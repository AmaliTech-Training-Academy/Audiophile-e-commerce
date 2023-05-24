# from django.urls import include, path
# from rest_framework import routers
# from ecommerce.views import CategoryViewSet, ProductViewSet, CartViewSet

# router = routers.defaultRouter()
# router.register(r'categories', CategoryViewSet)
# router.register(r'products', ProductViewSet)
# router.register(r'cart', CartViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from .views import CategoryAPIView, ProductAPIView, CartAPIView, CartItemAPIView

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),
    path('categories/', CategoryAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category-detail'),
    path('carts/', CartAPIView.as_view(), name='cart-list'),
    path('carts/<int:pk>/', CartAPIView.as_view(), name='cart-detail'),
    path('cart-items/', CartItemAPIView.as_view(), name='cartitem-list'),
    path('cart-items/<int:pk>/', CartItemAPIView.as_view(), name='cartitem-detail'),
]

