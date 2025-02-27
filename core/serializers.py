from rest_framework import serializers
from .models import Client, Product, Sale, Avaliation


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"


class AvaliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliation
        fields = "__all__"
