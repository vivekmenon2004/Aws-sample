from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MobilePhone(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
        ('refurbished', 'Refurbished'),
    ]

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='phones')
    model_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    storage = models.CharField(max_length=50)          # e.g. "128GB"
    ram = models.CharField(max_length=50)              # e.g. "8GB"
    battery = models.CharField(max_length=50)          # e.g. "5000mAh"
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='new')
    in_stock = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand.name} {self.model_name}"
