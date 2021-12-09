from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    typ = models.CharField(max_length=250)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Registration"