from django.shortcuts import render
from customers .models import Customer
from products .models import Product



def admin_index(request):
    template_name = 'app/index.html'
    context = {
        "is_admin_index" : True,
    }
    return render(request,template_name,context)


def customers_view(request):
    customers = Customer.objects.filter(is_active=True) 
    template_name = 'app/customers-view.html'
    context = {
        "is_customers_view" : True,
        "customers" : customers,
    }
    return render(request,template_name,context)


def products_view(request):
    products = Product.objects.filter(is_active=True)
    template_name = 'app/products-view.html'
    context = {
        "is_products_view" : True,
        "products" : products,
    }
    return render(request,template_name,context)