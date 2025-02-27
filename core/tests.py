from django.test import TestCase

from .models import Client, Product


class ClientModelTest(TestCase):
    def test_create_client(self):
        client = Client.objects.create(
            name="Carlos eduardo", cpf="115.447.944-65", date_birth="1998-05-12"
        )
        self.assertEqual(client.name, "Carlos eduardo")
        self.assertEqual(client.cpf, "115.447.944-65")


class ProductModelTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(
            product_name="Notebook", category="Eletronicos", price_product=3500.00
        )
        self.assertEqual(product.product_name, "Notebook")
        self.assertEqual(product.category, "Eletronicos")
        self.assertEqual(product.price_product, 3500.00)
