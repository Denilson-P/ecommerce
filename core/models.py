from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    date_birth = models.DateField()

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price_product = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale {self.id} - {self.client.name}"
