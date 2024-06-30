# exec(open(r"C:\Users\DELL\open_source\price_comparison\product\db_shell.py").read())
from product.models import Category, SubCategory, Retailer, Product, ProductPrice

# creating categories
electronics = Category.objects.create(name="electronics")
fashion = Category.objects.create(name="fashion")

# creating sub-categories
mobiles = SubCategory.objects.create(name="mobiles", category=electronics)
laptops = SubCategory.objects.create(name="laptops", category=electronics)
mens_clothing = SubCategory.objects.create(
    name="mens_clothing", category=fashion)

# creating retailer
store1 = Retailer.objects.create(
    name="Store1", website="https://www.store1.com")
store2 = Retailer.objects.create(
    name="Store2", website="https://www.store2.com")

# creating product
product_a = Product.objects.create(
    name="Product A", description="Description for Product A", subcategory=mobiles)
product_b = Product.objects.create(
    name="Product B", description="Description for Product B", subcategory=laptops)
product_c = Product.objects.create(
    name="Product C", description="Description for Product C", subcategory=mobiles)
product_d = Product.objects.create(
    name="Product D", description="Description for Product D", subcategory=mens_clothing)

# creating product_price
ProductPrice.objects.create(product=product_a, retailer=store1, price=100, cashback=15)
ProductPrice.objects.create(product=product_a, retailer=store2, price=105, cashback=10)
ProductPrice.objects.create(product=product_b, retailer=store1, price=205, cashback=5)
ProductPrice.objects.create(product=product_b, retailer=store2, price=200, cashback=10)
ProductPrice.objects.create(product=product_c, retailer=store1, price=165, cashback=5)
ProductPrice.objects.create(product=product_c, retailer=store2, price=155, cashback=10)
ProductPrice.objects.create(product=product_d, retailer=store1, price=175, cashback=15)
ProductPrice.objects.create(product=product_d, retailer=store2, price=185, cashback=10)


