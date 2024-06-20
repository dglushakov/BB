from django.db import models


# Create your models here.

class NVR(models.Model):
    ip = models.CharField(max_length=100, unique=True)
    port = models.IntegerField(default=80)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=200, editable=False)

    def __str__(self):
        return self.name
