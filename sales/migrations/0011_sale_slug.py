# Generated by Django 3.2.5 on 2021-07-16 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0010_auto_20210715_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
