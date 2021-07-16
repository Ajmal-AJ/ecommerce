from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('web.urls',namespace='web')),
    path('main/',include('main.urls',namespace='main')),
    path('products/',include('products.urls',namespace='products')),
    path('sales/',include('sales.urls',namespace='sales')),
    path('customers/',include('customers.urls',namespace='customers')),
    path('vendors/',include('vendors.urls',namespace='vendors')),
    path('app/',include('app.urls',namespace='app')),

    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('registration.backends.default.urls')),

    path('',include('demo.urls',namespace='demo')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
