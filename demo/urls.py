from django.urls import include, path
from django.views.generic import TemplateView

app_name = 'demo'

urlpatterns = [
    path('about.html/', TemplateView.as_view(template_name="demo/about.html")),
    path('account.html/', TemplateView.as_view(template_name="demo/account.html")),
    path('authorization-create-account.html/', TemplateView.as_view(template_name="demo/authorization-create-account.html")),
    path('authorization-login.html/', TemplateView.as_view(template_name="demo/authorization-login.html")),
    path('authorization-toggle-form.html/', TemplateView.as_view(template_name="demo/authorization-toggle-form.html")),
    path('authorization.html/', TemplateView.as_view(template_name="demo/authorization.html")),
    path('blog-2column.html/', TemplateView.as_view(template_name="demo/blog-2column.html")),
    path('blog-3column.html/', TemplateView.as_view(template_name="demo/blog-3column.html")),
    path('blog-no-column.html/', TemplateView.as_view(template_name="demo/blog-no-column.html")),
    path('blog-post.html/', TemplateView.as_view(template_name="demo/blog-post.html")),
    path('blog-right-column.html/', TemplateView.as_view(template_name="demo/blog-right-column.html")),
    path('blog.html/', TemplateView.as_view(template_name="demo/blog.html")),
    path('cart.html/', TemplateView.as_view(template_name="demo/cart.html")),
    path('coming-soon.html/', TemplateView.as_view(template_name="demo/coming-soon.html")),
    path('contacts.html/', TemplateView.as_view(template_name="demo/contacts.html")),
    path('faq.html/', TemplateView.as_view(template_name="demo/faq.html")),
    path('gallery-2column.html/', TemplateView.as_view(template_name="demo/gallery-2column.html")),
    path('gallery-4column.html/', TemplateView.as_view(template_name="demo/gallery-4column.html")),
    path('gallery-5column.html/', TemplateView.as_view(template_name="demo/gallery-5column.html")),
    path('gallery.html/', TemplateView.as_view(template_name="demo/gallery.html")),
    path('gift-card.html/', TemplateView.as_view(template_name="demo/gift-card.html")),
    path('index-02.html/', TemplateView.as_view(template_name="demo/index-02.html")),
    path('index-03.html/', TemplateView.as_view(template_name="demo/index-03.html")),
    path('index-04.html/', TemplateView.as_view(template_name="demo/index-04.html")),
    path('index-05.html/', TemplateView.as_view(template_name="demo/index-05.html")),
    path('index-06.html/', TemplateView.as_view(template_name="demo/index-06.html")),
    path('index-skin-accessories.html/', TemplateView.as_view(template_name="demo/index-skin-accessories.html")),
    path('index-skin-furniture.html/', TemplateView.as_view(template_name="demo/index-skin-furniture.html")),
    path('index-skin-techstore.html/', TemplateView.as_view(template_name="demo/index-skin-techstore.html")),
    path('index-skin-wheels.html/', TemplateView.as_view(template_name="demo/index-skin-wheels.html")),
    path('index.html/', TemplateView.as_view(template_name="demo/index.html")),
    path('listing-2-per-row.html/', TemplateView.as_view(template_name="demo/listing-2-per-row.html")),
    path('listing-4-per-row.html/', TemplateView.as_view(template_name="demo/listing-4-per-row.html")),
    path('listing-no-banner.html/', TemplateView.as_view(template_name="demo/listing-no-banner.html")),
    path('listing-no-col.html/', TemplateView.as_view(template_name="demo/listing-no-col.html")),
    path('listing-right-col.html/', TemplateView.as_view(template_name="demo/listing-right-col.html")),
    path('listing-sticky-filter.html/', TemplateView.as_view(template_name="demo/listing-sticky-filter.html")),
    path('listing-sticky-filters-row.html/', TemplateView.as_view(template_name="demo/listing-sticky-filters-row.html")),
    path('listing.html/', TemplateView.as_view(template_name="demo/listing.html")),
    path('lookbook.html/', TemplateView.as_view(template_name="demo/lookbook.html")),
    path('myaccount-addresses.html/', TemplateView.as_view(template_name="demo/myaccount-addresses.html")),
    path('myaccount-addresses2.html/', TemplateView.as_view(template_name="demo/myaccount-addresses2.html")),
    path('myaccount-order.html/', TemplateView.as_view(template_name="demo/myaccount-order.html")),
    path('myaccount.html/', TemplateView.as_view(template_name="demo/myaccount.html")),
    path('page404.html/', TemplateView.as_view(template_name="demo/page404.html")),
    path('password-recovery.html/', TemplateView.as_view(template_name="demo/password-recovery.html")),
    path('product-2.html/', TemplateView.as_view(template_name="demo/product-2.html")),
    path('product-3.html/', TemplateView.as_view(template_name="demo/product-3.html")),
    path('product-4.html/', TemplateView.as_view(template_name="demo/product-4.html")),
    path('product-5.html/', TemplateView.as_view(template_name="demo/product-5.html")),
    path('product-6.html/', TemplateView.as_view(template_name="demo/product-6.html")),
    path('product-7.html/', TemplateView.as_view(template_name="demo/product-7.html")),
    path('product-8.html/', TemplateView.as_view(template_name="demo/product-8.html")),
    path('product.html/', TemplateView.as_view(template_name="demo/product.html")),
    path('typography.html/', TemplateView.as_view(template_name="demo/typography.html")),
]