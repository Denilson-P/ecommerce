from django.contrib import admin
from .models import Client, Product, Sale, Avaliation


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "cpf", "date_birth")
    search_fields = ("name", "cpf")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "category", "price_product")
    search_fields = ("product_name", "category")


@admin.register(Sale)
class SaleAmin(admin.ModelAdmin):
    list_display = ("client", "product", "amount", "sale_date")
    list_filter = ("sale_date",)


@admin.register(Avaliation)
class AvaliationAdmin(admin.ModelAdmin):
    list_display = ("product", "client", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("product__product_name", "client__name")
    