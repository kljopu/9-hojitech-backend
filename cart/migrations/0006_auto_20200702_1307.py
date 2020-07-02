# Generated by Django 3.0.7 on 2020-07-02 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_account_product_price'),
        ('cart', '0005_auto_20200702_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDeliveryAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
            options={
                'db_table': 'user_deilivery_address',
            },
        ),
        migrations.AlterField(
            model_name='userorder',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.UserDeliveryAddress'),
        ),
    ]