# Generated by Django 4.1.3 on 2023-05-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(max_length=12, unique=True),
        ),
    ]
