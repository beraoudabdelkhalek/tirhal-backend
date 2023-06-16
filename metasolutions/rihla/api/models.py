from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.
class Utilizer(models.Model):
    email=models.CharField(max_length=255)
    role=models.CharField(max_length=255,default='touriste')
    password=models.CharField(max_length=63)
    phone=models.CharField(max_length=63,default="0")
    fullname=models.CharField(max_length=63)
    # def __str__(self):
    #     return self.fullname
    
class Region(models.Model):
    code=models.IntegerField(default=60)
    wilaya=models.CharField(max_length=63)
    idUser=models.ForeignKey(Utilizer,on_delete=models.SET_NULL,null=True,blank=True)
    latitude=models.FloatField(null=True,blank=True)
    longitude=models.FloatField(null=True,blank=True)

class Place(models.Model):
    idRegion=models.ForeignKey(Region,on_delete=models.CASCADE,null=True,blank=True)
    idUtilizer=models.ForeignKey(Utilizer,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=63)
    category=models.CharField(max_length=63)
    theme=models.CharField(max_length=63,null=True,blank=True)
    description=models.TextField(max_length=4064,null=True,blank=True)
    latitude=models.FloatField()
    longitude=models.FloatField()
    timefrom=models.TimeField(null=True,blank=True)
    timeto=models.TimeField(null=True,blank=True)

class Image(models.Model):
    idPlace=models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='pictures',null=True,blank=True)
    link=models.CharField(max_length=512,null=True,blank=True)

class Favorite(models.Model):
    idUtilizer=models.ForeignKey(Utilizer,related_name='favorites', on_delete=models.CASCADE)
    idPlace=models.ForeignKey(Place,on_delete=models.CASCADE)

class Comment(models.Model):
    idUtilizer=models.ForeignKey(Utilizer, on_delete=models.CASCADE)
    idPlace=models.ForeignKey(Place,related_name='comments', on_delete=models.CASCADE)
    pubdate=models.DateTimeField(default=timezone.now())
    comment=models.TextField(blank=True,null=True,max_length=4064)

class Rating(models.Model):
    idUtilizer=models.ForeignKey(Utilizer, on_delete=models.CASCADE)
    idPlace=models.ForeignKey(Place,related_name='ratings', on_delete=models.CASCADE)
    value=models.FloatField(null=True,blank=True)

class Transport(models.Model):
    idPlace=models.ForeignKey(Place,on_delete=models.CASCADE)
    type=models.CharField(max_length=255)
    number=models.CharField(max_length=255)
    placefrom=models.CharField(max_length=255)
    placeto=models.CharField(max_length=255)
    distance=models.FloatField(null=True,blank=True)

class Event(models.Model):
    idRegion=models.ForeignKey(Region,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    datefrom=models.DateTimeField()
    dateto=models.DateTimeField()
    place=models.CharField(max_length=255)


    


