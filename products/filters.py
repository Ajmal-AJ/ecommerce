import django_filters as filters
from django import forms
from .models import Category, Product, SubCategory
from main .models import Brand
class ProductFilter(filters.FilterSet):

    category = filters.ModelChoiceFilter(
        queryset=SubCategory.objects.filter(is_active=True),
        empty_label= ('All'),
        widget=forms.Select(attrs={'class': 'form-control','onchange' :"this.form.submit()"}))

    brand = filters.ModelChoiceFilter(
        queryset=Brand.objects.filter(is_active=True),
        empty_label= ('All'),
        widget=forms.Select(attrs={'class': 'form-control','onchange' :"this.form.submit()"}))

    class Meta:
        model = Product
        fields = {'category',}
