# Generated by Django 3.2.5 on 2021-07-09 06:57

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(upload_to='images/category/'),
        ),
    ]
