from django.urls import include, path

from . import views

app_name = 'products'

urlpatterns = [
    path('',views.products,name='products'),
    path('category/<str:slug>/',views.view_category,name='view_category'),
    path('product-details/<str:slug>/',views.product_details,name='product_details'),
    
]
