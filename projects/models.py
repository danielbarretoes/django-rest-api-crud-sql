from django.db import models

# Create your models here.
# Class Project permite crear una tabla en la base de datos conectada a Django.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tegnology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)