from django.contrib import admin
from django.apps import apps
from .models import Slider,Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('heading', 'slider_type')
        }),
        ('Image Options', {
            'classes': ('collapse',),
            'fields': ('subheading', 'description','image'),
        }),
        ('Video Options', {
            'classes': ('collapse',),
            'fields': ('video','background_image'),
        }),
    )