from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class Client(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex=r"^\d{3}\.\d{3}\.\d{3}-\d{2}$",
                message="CPF deve estar no formato 000.000.000-00",
            )
        ],
        unique=True,
    )
    email = models.EmailField(unique=True, null=True)
    date_birth = models.DateField()

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Eletrônicos", "Eletrônicos"),
        ("Roupas", "Roupas"),
        ("Alimentos", "Alimentos"),
        ("Livros", "Livros"),
    ]

    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price_product = models.DecimalField(max_digits=10, decimal_places=2)

    def average_rating(self):
        ratings = self.avaliations.all().values_list("rating", flat=True)
        return round(sum(ratings) / len(ratings), 2) if ratings else 0.0

    def __str__(self):
        return self.product_name


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale {self.id} - {self.client.name}"


class Avaliation(models.Model):
    product = models.ForeignKey(Product, related_name="avaliation", on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.name} - {self.product.product_name} ({self.rating})"
