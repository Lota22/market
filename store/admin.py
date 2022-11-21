from django.contrib import admin
from . models import *

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','product', 'title_g','price','quantity', 'amount','paid', 'order_no', 'payment_date']
admin.site.register(Cart, CartAdmin) 

class PaymentAdmin(admin.ModelAdmin):
    list_display= ['id','user','first_name','last_name','paid','amount','phone','pay_code','shop_code','payment_date','admin_update','admin_note']

admin.site.register(Payment,PaymentAdmin)    
