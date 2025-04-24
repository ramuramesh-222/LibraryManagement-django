from django.db import models

# Create your models here.
class Product(models.Model):

    product_name = models.CharField(max_length=200, null=True)
    product_code = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=0)
    gst = models.IntegerField(default=0)
    food_product = models.BooleanField(default=False)
    pictures = models.ImageField(null=True,upload_to='images/') 
    
    
    
    def __str__(self):

        return self.product_name    