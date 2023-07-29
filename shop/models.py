from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=200)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
    
class Cart(models.Model):
    Cprod_id = models.IntegerField(unique=True)
    Cprod_name = models.CharField(max_length=20)
    Cprice = models.IntegerField(default=0)
    Cdesc = models.CharField(max_length=200)
    Cimage = models.ImageField(upload_to="shop/images",default="")
    Cquantity = models.IntegerField(default=1)

    def __str__(self):
        return self.Cprod_name
    