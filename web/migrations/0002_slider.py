# Generated by Django 3.2.5 on 2021-07-08 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=128)),
                ('subheading', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/slider')),
                ('video', models.FileField(blank=True, null=True, upload_to='inages/slider/videos')),
            ],
        ),
    ]
