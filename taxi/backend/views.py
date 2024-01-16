from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    ordering = ['-created']
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    

class CategoryList(ListView):
    model = Product
    template_name = 'category.html'
    context_object_name = 'products'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.filter(category=self.kwargs['category_id'])

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(id=self.kwargs['category_id'])
        context['category'] = cat
        context["categories"] = Category.objects.all()
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    