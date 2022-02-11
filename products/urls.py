from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='home'),
    path("index",views.index),
    path("products",views.products,name='products'),
    path("categories/<slug:slug>",views.products_by_categories,name='products_by_categories'),
    path("products/<slug:slug>",views.product_details,name='product_details')
]