from django.db import models


class ProductDB(models.Model):
    title = models.CharField(max_length=65)
    price = models.DecimalField(max_digits=65, decimal_places=2)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title
