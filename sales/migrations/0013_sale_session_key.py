# Generated by Django 3.2.5 on 2021-07-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_remove_sale_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='session_key',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
