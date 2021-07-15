from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import mark_safe
from versatileimagefield.fields import VersatileImageField

class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)


class Slider(models.Model):
    SLIDER_TYPE_CHOICES = (('image','image'),('video','video'))

    heading = models.CharField(max_length=128)
    slider_type = models.CharField(max_length=128, choices=SLIDER_TYPE_CHOICES)

    subheading = models.CharField(max_length=128, blank=True,null=True)
    description = models.CharField(max_length=128, blank=True,null=True)
    image = VersatileImageField(upload_to='images/slider', blank=True,null=True)

    video = models.FileField(upload_to='videos/slider', blank=True,null=True)
    background_image = VersatileImageField(upload_to='images/slider',blank=True,null=True)

    def __str__(self):
        return str(self.heading)

