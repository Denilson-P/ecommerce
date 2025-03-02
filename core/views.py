from rest_framework import viewsets, permissions, filters

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
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    serarch_fields = ["name", "cpf", "email"]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["product_name", "category"]


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [permissions.IsAuthenticated]


class AvaliationViewSet(viewsets.ModelViewSet):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer
    permission_classes = [permissions.IsAuthenticated]
