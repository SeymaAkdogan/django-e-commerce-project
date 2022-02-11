from ast import Not
from pydoc import cram
from django.http import HttpResponse
from django.shortcuts import redirect, render
from cart.models import CartItem,Cart
from products.models import Product 
from django.http import HttpResponseRedirect

def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        total_price=0
        if cart:
            cartItems = CartItem.objects.filter(cart=cart[0])
            for cartItem in cartItems:
                total_price += float(cartItem.price) * float(cartItem.quantity)
            return render(request,'cart/cartList.html',{
                'cartItems' : cartItems,
                'total_price' : total_price
            })
        else:
            return render(request,'cart/cartList.html')
    else:
        return redirect('home')

def add_to_cart(request,productId):
    if request.user.is_authenticated:
        product = Product.objects.get(id=productId)
        cart = Cart.objects.filter(user=request.user)
        if cart:
            product_count = CartItem.objects.filter(product=product,cart=cart[0])
            if product_count:
                product_count[0].quantity += 1
                product_count[0].save()
            else:
                cartItem = CartItem.objects.create(product=product,quantity=1,price=product.price,cart=cart[0])
                cartItem.save()
        else:
            cart = Cart.objects.create(user=request.user)
            cart.save()
            cartItem = CartItem.objects.create(product=product,quantity=1,price=product.price,cart=cart)
            cartItem.save()

        return redirect('cart')
    else:
        return redirect('login')

def decrease_quantity_product(request,productId):
    if request.user.is_authenticated:
        product = Product.objects.get(id=productId)
        cart = Cart.objects.filter(user=request.user)
        if cart:
            product_count = CartItem.objects.filter(product=product,cart=cart[0])
            if product_count:
                if product_count[0].quantity >0:
                    product_count[0].quantity -= 1
                    if product_count[0].quantity == 0:
                        remove_from_cart(request=request,productId=productId)
                    else:
                        product_count[0].save()
        return redirect('cart')
    else:
        return redirect('login')


def remove_from_cart(request,productId):
    if request.user.is_authenticated:
        product = Product.objects.get(id=productId)
        cart = Cart.objects.filter(user=request.user)
        if cart:
            product_count = CartItem.objects.get(product=product,cart=cart[0])
            if product_count is not None:
                product_count.delete()
            
        return redirect('cart')
    else:
        return redirect('login')

