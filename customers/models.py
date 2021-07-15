from django.db import models
from main.models import BaseModel, UUIDTaggedItem
from django.core.validators import MinValueValidator
from decimal import Decimal
from versatileimagefield.fields import VersatileImageField
from django.contrib.auth.models import User


class Customer(BaseModel):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=128)
    email = models.EmailField(blank=True,null=True)
    address = models.TextField()
    photo = VersatileImageField('Photo',blank=True,null=True,upload_to="images/customers")

    def __str__(self):
        return str(self.name)