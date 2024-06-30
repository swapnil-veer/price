from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "category"

class SubCategory(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "subcategory"

class Retailer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "retailer"



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "product"

class ProductPrice(models.Model):
    product = models.ForeignKey(Product, related_name='prices', on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, related_name='prices', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cashback = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.retailer.name} - ${self.price}"
    
    class Meta:
        db_table = "product_price"