from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length= 50)
    alter = models.CharField(max_length=50)
    primary_power = models.CharField(max_length=100)
    secondary_power = models.CharField(max_length=100)
    catchphrase = models.TextField()


    def __str__(self):
        return self.name