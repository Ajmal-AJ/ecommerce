# Generated by Django 3.2.5 on 2021-07-14 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_is_featured'),
        ('sales', '0003_saleitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleitem',
            name='product',
            field=models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
