# Generated by Django 4.1.3 on 2023-05-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_product_descrip_product_desc_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
    ]
