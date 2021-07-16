from django.db import models
from django.core.exceptions import ValidationError
from django.utils.html import mark_safe
from main.models import BaseModel, UUIDTaggedItem
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.urls import reverse


class Sale(BaseModel):
    customer =models.ForeignKey('customers.Customer',on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    discount = models.DecimalField(default=0.0,decimal_places=2,max_digits=15,validators=[MinValueValidator(Decimal('0.00'))]) 
    session_key = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse('app:sale_view', kwargs={'pk': self.pk})

    def get_sales_item(self):
        if SaleItem.objects.filter(sale=self).exists():
            return SaleItem.objects.filter(sale=self)
        else:
            return None

    def __str__(self):
        return str(self.customer)


class SaleItem(BaseModel):
    sale = models.ForeignKey(Sale, on_delete=models.PROTECT) 
    product = models.ForeignKey('products.Product',on_delete=models.PROTECT)
    quantity = models.DecimalField(default=0,decimal_places=0,max_digits=15,validators=[MinValueValidator(Decimal('0'))])
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product)
