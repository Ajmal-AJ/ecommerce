from django.db import models
from django.core.exceptions import ValidationError
from django.utils.html import mark_safe
from main.models import BaseModel, UUIDTaggedItem
from django.core.validators import MinValueValidator
from decimal import Decimal


class Sale(BaseModel):
    customer =models.ForeignKey('customers.Customer',on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    discount = models.DecimalField(default=0.0,decimal_places=2,max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    def __str__(self):
        return str(self.customer)


class SaleItem(BaseModel):
    sale = models.ForeignKey(Sale, on_delete=models.PROTECT) 
    product = models.ForeignKey('products.Product',on_delete=models.PROTECT)
    quantity = models.DecimalField(default=0,decimal_places=0,max_digits=15,validators=[MinValueValidator(Decimal('0'))])
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product)
