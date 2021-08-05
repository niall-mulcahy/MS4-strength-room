from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    recurring = models.BooleanField()
    objects = models.Manager()

    def __str__(self):
        return self.name
