from django.contrib import admin
from .models import Client, Product, Sale


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "cpf", "date_birth")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "category", "price_product")


@admin.register(Sale)
class SaleAmin(admin.ModelAdmin):
    list_display = ("client", "product", "amount", "sale_date")
