from django.db import models
from django.contrib.auth.models import User
# Create your models here.

length=255
class User_data(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    culture = models.CharField(max_length=length,default="")
    zone_champ = models.CharField(max_length=length,default="")
    stade = models.IntegerField(default=0)
    fine=models.DecimalField(max_digits=5, decimal_places=2)
    potential_stress=models.DecimalField(max_digits=5, decimal_places=2)
    stress=models.DecimalField(max_digits=5, decimal_places=2)
    acre_fine=models.DecimalField(max_digits=5, decimal_places=2,default=0)
    acre_potential_stress=models.DecimalField(max_digits=5, decimal_places=2,default=0)
    acre_stress=models.DecimalField(max_digits=5, decimal_places=2,default=0)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return "{}-{}".format(self.user,self.date)
    
    def plant_stress_area(self):
        return self.potential_stress+self.stress

    def plant_stress_acre(self):
        return self.acre_potential_stress+self.acre_stress
    