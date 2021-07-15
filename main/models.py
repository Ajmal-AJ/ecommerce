from uuid import uuid4
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Country(BaseModel):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = ('Countries')

    def __str__(self):
        return str(self.name)


class State(BaseModel):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Brand(BaseModel):
    brand_name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.brand_name)