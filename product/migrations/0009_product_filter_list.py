# Generated by Django 3.0.7 on 2020-06-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_productdescription_productspecification_productteaser_productvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='filter_list',
            field=models.ManyToManyField(related_name='product', through='product.ProductFilter', to='product.FilterList'),
        ),
    ]
