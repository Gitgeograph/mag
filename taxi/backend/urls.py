from django.urls import path
from .views import ProductListView, ProductDetail, CategoryList
urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product'),
    path('category/<int:category_id>', CategoryList.as_view(), name='category')
]
