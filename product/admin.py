from django.contrib import admin

from .models import Category, SubCategory, Retailer, Product, ProductPrice
# Register your models here.
admin.site.register([Category, SubCategory, Retailer, Product, ProductPrice])