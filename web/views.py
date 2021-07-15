from django.http import HttpResponse
from django.shortcuts import render
from .models import Slider
from products.models import Category
from products .views import view_category
from  products  import urls


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
