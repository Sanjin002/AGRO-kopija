from django.shortcuts import render
from rest_framework import viewsets
from .models import Crop, Category
from .serializers import CropSerializer, CategorySerializer

# viewsets je module
class CropView(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer