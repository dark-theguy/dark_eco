from django.urls import path
from .views import *
import random
app_name = 'amydo'

urlpatterns = [
    path('', IndexView.as_view(), name='index' ),
    path('product/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('cart', CartView.as_view(), name='my-cart'),
    path('checkout', CheckOutView.as_view(), name='checkout'),
    path('category/<str:slug>', CategoryView.as_view(), name='category'),
]