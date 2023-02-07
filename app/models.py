from django.db import models

class Glases(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='glasses/')
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.title
