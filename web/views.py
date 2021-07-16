from django.http import HttpResponse
from django.shortcuts import render
from .models import Slider
from products.models import Category
from products .views import view_category
from  products  import urls
from sales .models import Sale, SaleItem


def index(request):
    categories = Category.objects.filter(is_active=True)
    sliders = Slider.objects.all()
    template_name = "web/index.html"
    context = {
        "is_index" : True,
        "sliders" : sliders,
        "categories" : categories,
    }
    return render(request, template_name, context)


def listing(request):
    categories = Category.objects.filter(is_active=True)
    template_name = "web/listing.html"
    context = {
        "is_listing" : True,
        "categories" : categories,
    }
    return render(request, template_name,context)


def add_cart(request, pk):
    user_session = request.session.session_key
    product = get_object_or_404(Product, pk=pk)
    if Sale.objects.filter(
            user_session=user_session,
            product=product,
            placed=False).exists():
        quantity = 1
        order_item = Sale.objects.get(
            user_session=user_session, product=product, placed=False)
        order_item.quantity += quantity
        order_item.save()
        response_data = {
            'status': 'true',
            'title': 'Product Added',
            'message': 'Cart Successfully Updated.',
            'redirect': 'true',
            'redirect_url': reverse('products:index')
        }
    else:
        Sale(
            user_session=user_session,
            product=product,
            quantity=1,
        ).save()
        response_data = {
            'status': 'true',
            'title': 'Product Updated',
            'message': 'Cart Successfully Updated.',
            'redirect': 'true',
            'redirect_url': reverse('products:index')
        }
    return HttpResponse(json.dumps(response_data),content_type='application/javascript')








    context = {
        "add_cart" : True,
    }
    return render(request,context)