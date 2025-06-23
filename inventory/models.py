from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)  # Aynı isimde ürün eklenmesini engeller

    def __str__(self):
        return f"{self.id} - {self.name}"


class Stock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    wholeseller_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    retailer_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.item.name} - Qty: {self.quantity} - Price: {self.price}"
