from django.shortcuts import render

# Create your views here.
# class based view 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Product
from .serializers import ProductSerializer

class ProductList(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.BasePermission]

    def get(self,request):
        prod_list = Product.objects.all()
        ser_data  = ProductSerializer(prod_list, many = True)
        return Response(ser_data.data)
    