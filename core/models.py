from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField()
    subject=models.CharField(max_length=500)
    area=models.CharField(max_length=1000)
    def __str__(self):
        return self.name