from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Size,Review, Colour, Material 
from main .models import Brand
from .filters import  ProductFilter
from django.core.paginator import Paginator



def products(request):
    dataset = Product.objects.filter(is_active=True)
    product_filter = ProductFilter(request.GET, queryset=dataset)
    paginator = Paginator(product_filter.qs,6)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    categories = Category.objects.all()
    brands= Brand.objects.all()
    sizes = Size.objects.all() 
    template_name = 'products/products.html'
    context = {
        "is_products" : True,
        "products" : products,
        "product_filter" : product_filter,
        "categories" : categories,
        "brands" : brands,
        "sizes" : sizes,
    }
    return render(request, template_name,context)


def view_category(request,slug):
    category = get_object_or_404(Category,slug=slug)
    categories = Category.objects.all()
    brands= Brand.objects.all()
    sizes = Size.objects.all() 
    template_name = 'products/viewcategory.html'
    context = {
        "is_view_category" : True,
        "category" : category,
        "categories" : categories,
        "brands" : brands,
        "sizes" : sizes,
    }
    return render(request, template_name,context)


def product_details(request,slug):
    product = get_object_or_404(Product,slug=slug)
    sizes= Size.objects.all()
    materials = Material.objects.filter(is_active=True)
    template_name = 'products/product_details.html'
    context = {
        "Is_product" : True,
        "product" : product,
        "sizes" : sizes,
        "materials" : materials,
    }
    return render(request,template_name,context)
    