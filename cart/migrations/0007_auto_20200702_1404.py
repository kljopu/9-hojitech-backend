# Generated by Django 3.0.7 on 2020-07-02 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20200702_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='user_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.UserOrder'),
        ),
    ]
