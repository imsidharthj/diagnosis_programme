from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    weight = models.FloatField()
    allergy = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class Symptoms(models.Model):
    disease = models.ForeignKey(Disease, related_name='symptoms', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
