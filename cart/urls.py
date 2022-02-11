from django.urls import path
from . import views

urlpatterns = [
    path("cart",views.cart,name='cart'),
    path("cart/add/<int:productId>",views.add_to_cart,name='add_to_cart'),
    path("cart/decrease/<int:productId>",views.decrease_quantity_product,name='decrease_quantity_product'),
    path("cart/remove/<int:productId>",views.remove_from_cart,name='remove_from_cart')
]