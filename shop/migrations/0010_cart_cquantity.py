# Generated by Django 4.1.3 on 2023-07-03 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_rename_desc_cart_cdesc_rename_image_cart_cimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Cquantity',
            field=models.IntegerField(default=1),
        ),
    ]
