# Generated by Django 4.1.3 on 2023-07-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_cart_cquantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Cquantity',
            field=models.IntegerField(default=1),
        ),
    ]