# Generated by Django 3.2.5 on 2021-07-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_rename_type_slider_slider_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='images/slider/videos'),
        ),
    ]
