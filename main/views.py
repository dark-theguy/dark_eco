from itertools import product
from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, FormView, ListView,
                                  TemplateView, View)
from .models import *
# Create your views here.

class IndexView(TemplateView):
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(category__title = 'Drugs') 
        category = Category.objects.all()
        context["products"] = products
        context['category'] = category
        return context

class CartView(TemplateView):
	template_name = 'main/cart.html'

class ProductDetailView(DetailView):
    template_name = 'main/product_detail.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        p = Product.objects.get(slug = slug)
        cat = p.category
        products = Product.objects.filter(category = cat)
        context["products"] = products
        return context
        
class CategoryView(TemplateView):
    template_name = 'main/category.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs['slug']
        products = Product.objects.filter(category__slug = slug)
        context["products"] = products
        return context
    

class CheckOutView(TemplateView):
	template_name = 'main/checkout.html'

class SideBar(View):
    template_name = 'sidebar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all() 
        return context
    