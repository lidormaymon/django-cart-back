from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)

 
    def __str__(self):
           return self.desc
    
class Orders(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
     amount = models.IntegerField()
     desc = models.CharField(max_length=50,null=True,blank=True)
     price = models.IntegerField()


     def __str__(self):
         return self.price

class Deliveries(models.Model):
     order_id = models.DecimalField(max_digits=5, decimal_places=2)
     delivery_date = models.DateTimeField(auto_now_add=True)
     delivry_staff = models.CharField(max_length=50)
     def __str__(self):
          return self.order_id
