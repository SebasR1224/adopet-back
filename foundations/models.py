from django.db import models

# Create your models here.
class Foundation(models.Model):
    name = models.CharField(max_length=255)
    introduction = models.TextField(blank=True)
    history = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    webSite = models.URLField(max_length=255)
    nit = models.CharField(max_length=10)
    employeeCount = models.IntegerField(default=0)
    foundationFoundingDate = models.DateField()
    animalsAssistedCount =  models.IntegerField(default=0)
    currentAnimalsAssistedCount =  models.IntegerField(default=0)
    limitAnimalsAssistedCount =  models.IntegerField(default=0)
    foundationRating =  models.IntegerField(default=0)

