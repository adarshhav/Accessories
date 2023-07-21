from django.db import models
from store.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default="cart")
    # quantity=models.IntegerField(default=1)
    
    # @property
    # def qtyprice(self):
    #     tot=self.product.price*self.quantity
    #     return tot
        
        
        
    
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    address=models.CharField(max_length=300)
    options=(
        ("Order placed","Order placed"),
        ("Shipped","Shipped"),
        ("Out for Delivery","Out for Delivery"),
        ("Delivered","Delivered"),
        ("Cancel","Cancel")
    )
    status=models.CharField(max_length=100,choices=options,default="Order Placed")
    date=models.DateField(auto_now_add=True)