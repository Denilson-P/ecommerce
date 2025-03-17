from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response


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
    
    @action(detail=True, methods=["get"])
    def avaliation(self, request, pk=None):
        product = self.get_object()
        serializer = AvaliationSerializer(product.avaliation.all(), many=True)
        return Response(serializer.data)
    


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [permissions.IsAuthenticated]


class AvaliationViewSet(viewsets.ModelViewSet):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer
    permission_classes = [permissions.IsAuthenticated]
