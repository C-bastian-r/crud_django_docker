from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length = 30, blank = False, null = False)
    description = models.TextField()
    salary = models.FloatField(blank = False ,null = False)
    def __str__(self):
        return self.name

class Employ(models.Model):
    name = models.CharField(max_length = 50, blank = False, null = False)
    phone = models.CharField(max_length = 11)
    address = models.CharField(max_length = 30, blank = True)
    job = models.ForeignKey(Job, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
