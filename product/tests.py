from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product,Category, SubCategory
from django.urls import reverse
from rest_framework import status
from .serializers import ProductSerializer

# Create your tests here.
from rest_framework.test import APITestCase

class ProductListTest(APITestCase):
    def setUp(self):
        # Created user 
        self.user = User.objects.create_user(username="abc", password="1234")
        # Created product
        self.electronics = Category.objects.create(name="electronics")
        self.mobiles = SubCategory.objects.create(name="mobiles", category=self.electronics)
        self.product_A = Product.objects.create(name="Product A", description="Description for Product A", subcategory=self.mobiles)
        self.product_B = Product.objects.create(name="Product B", description="Description for Product B", subcategory=self.mobiles)
        # Created Url
        self.url = reverse('product_list')

    def test_product_list(self):
        # make user to login
        self.client.login(username = "abc", password = "1234")

        response = self.client.get(self.url)
        products = Product.objects.all()
        ser = ProductSerializer(products, many=True)

        # Check for status code 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ser.data, response.data)

