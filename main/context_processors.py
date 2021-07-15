from sales .models import SaleItem


def main_context(request):
    cart_items = SaleItem.objects.filter(sale__customer__user=request.user,is_ordered=False)
    print(cart_items)
    return {
        'cart_items' :cart_items,
        'domain' : request.META['HTTP_HOST'],
        'enable_newsletter_pop_up' : False, 
    }