# Generated by Django 4.1.3 on 2023-07-03 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_cart_cquantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Cquantity',
            field=models.IntegerField(default=1),
        ),
    ]