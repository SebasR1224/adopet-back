from django.db import models

# Create your models here.
class Animals(models.Model):
    nombre = models.CharField(max_length=255)
    age = models.CharField(max_length=2)
    coatColor = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    breedortype = models.CharField(max_length=50)
    rescueStory = models.TextField(blank=False)
    rescueDate = models.DateTimeField(auto_now=False)
    healtCondition = models.CharField(max_length=255)
    rescuePlace = models.CharField(max_length=255)
    isAdoptable = models.BooleanField(default=False)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre