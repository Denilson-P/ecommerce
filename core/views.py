from rest_framework import viewsets

from .serializers import (
    ClientSerializer,
    ProductSerializer,
    SaleSerializer,
    AvaliationSerializer,
)
from .models import Client, Product, Sale, Avaliation


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class AvaliationViewSet(viewsets.ModelViewSet):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer
