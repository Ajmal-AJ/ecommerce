# Generated by Django 3.2.5 on 2021-07-15 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_alter_sale_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleitem',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
    ]