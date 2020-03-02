from django.db import models
from account.models import Account
# Create your models here.

class Notice(models.Model):
    ownerId=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="OwnerUser",verbose_name="Owner User")
    locationId=models.ForeignKey('notice.Location',on_delete=models.CASCADE)
    image=models.CharField(max_length=500,verbose_name="ImageUrl")
    date=models.DateTimeField(auto_now=True,verbose_name="Datetime")
    title=models.CharField(max_length=300,verbose_name="Notice Title")
    description=models.TextField(verbose_name="Notice Description")
    lostType=models.CharField(choices=[('Human','Human'),('Animal','Animal')],default='Animal',verbose_name='Type',max_length=6)
    #typeId=models.ForeignKey() to do
    award=models.CharField(max_length=100,verbose_name="Award")
    isFind=models.BooleanField()
    finderId=models.ForeignKey(Account,on_delete=models.CASCADE,blank=True,related_name="FinderUser",verbose_name="Finder User")

    def __str__(self):
        return self.title

class Location(models.Model):
    latitude=models.CharField(max_length=100,verbose_name="Latitude")
    longitude=models.CharField(max_length=100,verbose_name="Longitude")
    city=models.CharField(max_length=50,verbose_name="City")
    district=models.CharField(max_length=50,verbose_name="District")
    
    def __str__(self):
        return self.city
class Human(models.Model):
    name=models.CharField(max_length=100,verbose_name="Name")
    surname=models.CharField(max_length=100,verbose_name="Surname")
    gender=models.CharField(max_length=10,verbose_name="Gender")
    age=models.CharField(max_length=10,verbose_name="Age")
    clothes=models.TextField(verbose_name="Clothes")

    def __str__(self):
        return self.name+" "+self.surname

class Animal(models.Model):
    animalType=models.CharField(max_length=100,verbose_name="Animal Type")
    race=models.CharField(max_length=50,verbose_name="Animal race")
    color=models.CharField(max_length=20,verbose_name="Animal color")

    def __str__(self):
        return self.animalType+" "+self.race+" "+self.color
