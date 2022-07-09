from django.db import models

# Create your models here.

class Reg(models.Model):
    First_name=models.CharField('First Name',max_length=150)
    Last_name=models.CharField('Last Name',max_length=150)
    Date_Of_Birth=models.DateField('Date Of Birth')
    Gender=models.CharField(max_length=15)
    Address=models.TextField('Address', blank=False)
    City=models.CharField(max_length=30)
    State= models.CharField(max_length=30)
    PINCODE=models.IntegerField(max_length=6)
    Mobile_number=models.IntegerField(max_length=10)

    def __str__(self):
        return self.First_name +''+ self.Last_name

# class Details(models.Model):
    



    
