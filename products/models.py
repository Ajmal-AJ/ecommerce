from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import mark_safe
from taggit.managers import TaggableManager
from main.models import BaseModel, UUIDTaggedItem
from decimal import Decimal
from django.core.validators import MinValueValidator
from tinymce.models import HTMLField
from colorfield.fields import ColorField
from versatileimagefield.fields import VersatileImageField
from django.urls import reverse
from django.template.defaultfilters import slugify


def generate_id():
    last_product = Product.objects.last()
    if not last_product:
         return 'P0001'
    product_id = last_product.product_id
    product_int = int(product_id.split('P')[-1])
    new_product_int = product_int + 1
    new_product_id = 'P' + str(new_product_int).zfill(4)
    return new_product_id


class Category(BaseModel):
    category_id = models.IntegerField()
    title = models.CharField(max_length=128)
    image = VersatileImageField(upload_to='images/category/')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = ('Categories')

    def get_absolute_url(self):
        return reverse('products:view_category', kwargs={'slug': self.slug})

    def get_featured_products(self):
        if Product.objects.filter(category__category=self,is_featured=True).exists():
            return Product.objects.filter(category__category=self)
        else:
            return None

    def get_products(self):
        if Product.objects.filter(category__category=self).exists():
            return Product.objects.filter(category__category=self)
        else:
            return None

    def __str__(self):
        return str(self.title)


class SubCategory(BaseModel):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = ('SubCategories')

    def get_products(self):
        if Product.objects.filter(category=self).exists():
            return Product.objects.filter(category=self)
        else:
            return None
    
    def __str__(self):
        return str(self.title)


class Product(BaseModel):
    product_id = models.CharField(max_length=128,default=generate_id,unique=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=128)
    brand = models.ForeignKey('main.Brand', on_delete=models.CASCADE)
    tags = TaggableManager(blank=True,through=UUIDTaggedItem)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    information = HTMLField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=15, validators=[MinValueValidator(Decimal('0.00'))])
    mrp = models.DecimalField(default=0.0, decimal_places=2, max_digits=15, validators=[MinValueValidator(Decimal('0.00'))])
    cost = models.DecimalField(default=0.0, decimal_places=2, max_digits=15, validators=[MinValueValidator(Decimal('0.00'))])
    opening_stock = models.DecimalField(default=0, decimal_places=0, max_digits=15, validators=[MinValueValidator(Decimal('0'))])
    current_stock = models.DecimalField(default=0, decimal_places=0, max_digits=15, validators=[MinValueValidator(Decimal('0'))])
    is_featured = models.BooleanField(default=True)

    def get_stock(self):
        return (self.opening_stock + self.current_stock)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_images(self):
        if ProductImage.objects.filter(product=self).exists():
            return ProductImage.objects.filter(product=self)
        else:
            return None
    
    def get_single_image(self):
        if ProductImage.objects.filter(product=self).exists():
            return ProductImage.objects.filter(product=self).first()
        else:
            return None

    def get_absolute_url(self):
        return reverse('products:product_details', kwargs={'slug': self.slug})
    
    def get_reviews(self):
        if  Review.objects.filter(product=self).exists():
            return  Review.objects.filter(product=self)
        else:
            return None

    def get_related_products(self):
        if Product.objects.filter(category=self.category).exists():
            return Product.objects.filter(category=self.category)
        else:
            return None

    def __str__(self):
        return str(self.title)


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_image')
    color = models.ForeignKey('products.Colour', on_delete=models.CASCADE)
    image = VersatileImageField(upload_to='images/products')

    def __str__(self):
        return str(self.product.title)


class Colour(BaseModel):
    title = models.CharField(max_length=128)
    color_code = ColorField(format='hexa')

    def __str__(self):
        return str(self.title)


class Review(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name= models.CharField(max_length=128)
    image = VersatileImageField(upload_to='images/reviews/',blank=True, null= True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Material(BaseModel):
    image = VersatileImageField(upload_to='images/matrials/')
    title = models.CharField(max_length=128)


    def __str__(self):
        return str(self.title)


class Size(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return str(self.title)


