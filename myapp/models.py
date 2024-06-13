from django.db import models

# Create your models here.
class KitchenInventory(models.Model):
    Productname=models.CharField(max_length=30,blank=False,null=True)
    Productqnt=models.IntegerField()
    Unitoffprd=models.CharField(max_length=30,blank=False,null=True)
    
    def __str__(self):
        return self.Productname + " " + str(self.Productqnt)
    
    
