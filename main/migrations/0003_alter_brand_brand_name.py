# Generated by Django 3.2.5 on 2021-07-09 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
