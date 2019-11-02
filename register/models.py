from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Create your models here.
length=250
class Station(models.Model):
    nom_station = models.CharField(max_length=length)

    def boxes(self):
        station=get_object_or_404(Station,id=self.id)
        boxes=Box.objects.filter(station=station)
        return boxes.count()
    
    def boxe_libre(self):
        station=get_object_or_404(Station,id=self.id)
        boxe_libre=Box.objects.filter(station=station,libre="yes")
        return boxe_libre.count()  
    
    def choice_box(self):
        station=get_object_or_404(Station,id=self.id)
        if Box.objects.filter(station=station,libre="yes").exists():
            box=Box.objects.filter(station=station,libre="yes")[0]
            return box
        else:
            return "none"

    def __str__(self):
        return self.nom_station


class Box(models.Model):
    station= models.ForeignKey(Station, on_delete=models.CASCADE)
    libre = models.CharField(max_length=length,default="yes")

    def __str__(self):
        return self.station.nom_station


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    code = models.IntegerField()
    njh = models.IntegerField(default='1')
    jh=models.CharField(max_length=length,default="jour(s)")
    
    def __str__(self):
        return self.user.first_name+"--station:"+self.box.station.nom_station+"--box numero:"+str(self.box.id)

    

  
