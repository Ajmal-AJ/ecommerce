# Generated by Django 3.2.5 on 2021-07-15 05:16

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_is_featured'),
        ('customers', '0005_alter_customer_email'),
        ('sales', '0009_auto_20210715_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.customer'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='quantity',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
    ]
