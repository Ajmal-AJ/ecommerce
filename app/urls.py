from django.urls import include, path

from . import views

app_name = 'app'

urlpatterns = [
    path('',views.admin_index,name='index'),
    path('customers-view/',views.customers_view,name='customers_view'),
    path('products-view/',views.products_view,name='products_view'),

    
]