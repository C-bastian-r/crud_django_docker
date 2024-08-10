from django.db import models

# Create your models here.
class Invoice(models.Model):
    name = models.CharField(max_length = 30, blank = False, null = False)
    description = models.TextField()
    value = models.FloatField()
    is_pay = models.BooleanField(default = False)

    def __str__(self):
        return self.name