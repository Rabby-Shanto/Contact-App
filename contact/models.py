from django.db import models

# Create your models here.
class Contact(models.Model):
    FullName = models.CharField(max_length=100)
    RelationShip = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=20)
    Address = models.CharField(max_length=500)

    def __str__(self):
        return self.FullName


