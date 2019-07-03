from django.db import models



class Stones(models.Model):
        client = models.CharField(max_length = 10)
        x = models.CharField(max_length = 10)
        y = models.IntegerField()

