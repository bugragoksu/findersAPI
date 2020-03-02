from django.db import models

# Create your models here.

class Account(models.Model):
    email=models.CharField(max_length=100,verbose_name="Email")
    pasword=models.CharField(max_length=100,verbose_name="Password")
    name=models.CharField(max_length=100,verbose_name="Name")
    surname=models.CharField(max_length=100,verbose_name="Surname")
    city=models.CharField(max_length=100,verbose_name="City")
    image=models.CharField(max_length=500,verbose_name="ImageUrl",blank=True)
    


    def __str__(self):
        return self.email


