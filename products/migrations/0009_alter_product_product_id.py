# Generated by Django 3.2.5 on 2021-07-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210709_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
