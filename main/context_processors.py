from sales .models import SaleItem


def main_context(request):
    if request.user.is_authenticated:
        cart_items = SaleItem.objects.filter(sale__customer__user=request.user,is_ordered=False)
    else:
        cart_items = []
    if not request.session.exists(request.session.session_key):
        request.session.create() 
    print(request.session.session_key)
    return {
        'cart_items' :cart_items,
        'domain' : request.META['HTTP_HOST'],
        'enable_newsletter_pop_up' : False, 
    }