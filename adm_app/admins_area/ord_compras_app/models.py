from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length = 30, blank = False, null = False)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name