from django.urls import include, path

from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index,name='index'),
    path('listing',views.listing,name='listing'),

]