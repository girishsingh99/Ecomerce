from django.shortcuts import render

# Create your views here.
from .models import Product
from .serializers import ProductSerialization
from rest_framework.viewsets import ModelViewSet

class ProductOperations(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization

