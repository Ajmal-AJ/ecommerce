from django.shortcuts import render, get_object_or_404
from customers .models import Customer
from products .models import Product, Category, Colour, Size, Material
from sales .models import Sale, SaleItem
from main .models import Brand
from django.contrib.auth.decorators import login_required


@login_required
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


def sales_list(request):
    sales_list = Sale.objects.filter(is_active=True) 
    template_name = 'app/sales-list.html'
    context = {
        "is_sale_list" : True,
        "sales_list" : sales_list,
    }
    return render((request), template_name, context)

def category_view(request):
    categories = Category.objects.filter(is_active=True)
    template_name = 'app/category-view.html'
    context = {
        "is_context_view" : True,
        "categories" : categories,
    }
    return render(request,template_name,context)

def sale_view(request,pk):
    sale_view = get_object_or_404(Sale,pk=pk)
    template_name = 'app/sales-view.html'
    context = {
        "is_sale_view" : True,
        "sale_view" : sale_view,
    }
    return render((request), template_name, context)


def brands_view(request):
    brands = Brand.objects.filter(is_active=True)
    template_name = 'app/brands-view.html'
    context = {
        "is_brands_view" : True,
        "brands" : brands,
    }
    return render(request,template_name,context)


def colors_view(request):
    colors = Colour.objects.filter(is_active=True)
    template_name = 'app/colors-view.html'
    context = {
        "is_colors_view" : True,
        "colors" : colors,
    }
    return render(request,template_name,context)


def sizes_view(request):
    sizes = Size.objects.filter(is_active=True)

    template_name = 'app/size-view.html'
    context = {
        "is_sizes_view" : True,
        "sizes" : sizes,
    }
    return render(request,template_name,context)


def material_view(request):
    materials = Material.objects.filter(is_active=True)

    template_name = 'app/material-view.html'
    context = {
        "is_material_view" : True,
        "materials" : materials,
    }
    return render(request,template_name,context)

