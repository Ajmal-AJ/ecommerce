from django.urls import include, path

from . import views

app_name = 'app'

urlpatterns = [
    path('',views.admin_index,name='index'),
    path('category-view/',views.category_view,name='category_view'),
    path('products-view/',views.products_view,name='products_view'),
    path('brands-view/',views.brands_view,name='brands_view'),
    path('colors-view/',views.colors_view,name='colors_view'),
    path('sizes-view/',views.sizes_view,name='sizes_view'),
    path('material-view/',views.material_view,name='material_view'),
    path('customers-view/',views.customers_view,name='customers_view'),
    path('sale-view/<str:pk>/',views.sale_view,name='sale_view'),
    path('sales-list/',views.sales_list,name='sales_list'),


    
]