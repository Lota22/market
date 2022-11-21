from django.contrib import admin
from . models import *


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display= ['id', 'full_name', 'email', 'message', 'status', 'sent','updated']
admin.site.register(Contact, ContactAdmin)    
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'img', 'slug']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title_r','slug', 'img_r', 'description', 'price', 'max_quantity', 'min_quantity' , 'size', 'display',
 'shoes', 'bags', 'perfume', 'cloth', 'uploaded']
admin.site.register(Product, ProductAdmin)     
