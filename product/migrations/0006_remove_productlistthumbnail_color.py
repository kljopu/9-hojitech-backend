# Generated by Django 3.0.7 on 2020-06-26 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200625_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlistthumbnail',
            name='color',
        ),
    ]
