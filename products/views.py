from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product,Category

def index(request):
    return render(request,'products/home.html',{
        'categories': Category.objects.all()
    })

def products(request):
    search_key = request.GET.get('search', None)
    result = []
    min_price= request.GET.get('min_price',None)
    max_price= request.GET.get('max_price',None)
    selected_category = request.GET.get('category',None)

    if search_key is not None:
        products_all = Product.objects.all()
        category_all = Category.objects.all()
        products=[]
        categories=[]

        for product in products_all:
            if search_key.lower() in product.name.lower():
                products.append(product)
            elif search_key.lower() in product.description.lower():
                products.append(product)

        for category in category_all:
            if search_key.lower() in category.name.lower():
                categories.append(category)

        if len(products)>0:
            return render(request,'products/products.html',{
                'products' : products,
                'categories' : Category.objects.all()
            })
        if len(categories)>0:
            return render(request,'products/home.html',{
                'categories': categories
            })

        if len(products) == 0 and len(categories) == 0:
            return render(request,'products/products.html',{
                'error' : 'No Product or Category',
                'products' : products,
                'categories' : Category.objects.all()
            })
    elif selected_category is not None and selected_category != 'Choose':
        products = Category.objects.get(name=selected_category).product_set.filter(is_active=True)
        min_price = float(min_price)
        max_price = float(max_price)
        for product in products:
            if min_price <= product.price and product.price <= max_price:
                result.append(product)
    elif min_price is not None and max_price is not None:
        products = Product.objects.filter(is_active=True)
        min_price = float(min_price)
        max_price = float(max_price)
        for product in products:
            if min_price <= product.price and product.price <= max_price:
                result.append(product)

    if len(result)>0:
        return render(request,'products/products.html',{
            'products' : result,
            'categories' : Category.objects.all(),
            'selected_category' : selected_category,
            'min_price': int(min_price),
            'max_price': int(max_price)
        })
    elif min_price is not None and max_price is not None and len(result) == 0:
        return render(request,'products/products.html',{
            'error' : 'No Product',
            'products' : result,
            'categories' : Category.objects.all(),
            'selected_category' : selected_category,
            'min_price': int(min_price),
            'max_price': int(max_price)
        })
    else:
        return render(request,'products/products.html',{
            'products':Product.objects.filter(is_active=True),
            'categories' : Category.objects.all()
        })

    

    
def products_by_categories(request,slug):
    return render(request,'products/products.html',{
        'products' : Category.objects.get(category_slug=slug).product_set.filter(is_active=True),
        'categories' : Category.objects.all()
    })

def product_details(request,slug):
    
    product = Product.objects.get(slug=slug)
    return render(request,'products/productdetail.html',{
        'product' : product
    })

