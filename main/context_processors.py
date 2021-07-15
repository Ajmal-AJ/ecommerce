def main_context(request):
    return {
        'domain' : request.META['HTTP_HOST'],
        'enable_newsletter_pop_up' : False, 
    }