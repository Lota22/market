
from django.db import models
from home.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title_g = models.CharField(max_length= 30, blank = True, null= True)
    price = models.FloatField()
    quantity = models.IntegerField()
    amount = models.IntegerField(null= True, blank=True)
    paid = models.BooleanField()
    order_no = models.CharField(max_length=60)
    payment_date = models.DateTimeField(auto_now_add=True)
    # cart = CartManage()

    # def __unicode__(self):
    #     return self.name

    def __str__(self):
        return self.title_g

    class Meta:
        db_table = 'cart'
        managed = True
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    paid = models.BooleanField()
    amount = models.IntegerField()
    phone = models.CharField(max_length=50)
    pay_code = models.CharField(max_length=100)
    shop_code = models.CharField(max_length=100)
    payment_date = models.DateTimeField(auto_now=True)
    admin_update = models.DateTimeField(auto_now_add=True)
    admin_note = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.user.username




