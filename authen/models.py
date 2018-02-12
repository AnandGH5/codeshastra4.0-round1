from django.db import models
from django.contrib.auth.models import User
import hashlib

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    age = models.CharField(max_length=150,blank=True)
    f1 = models.CharField(max_length=150,blank=True)
    f2 = models.CharField(max_length=150,blank=True)
    f3 = models.CharField(max_length=150,blank=True)
    gender = models.CharField(max_length=1,blank=True)
    phone=models.CharField(max_length=150,blank=True)
    profile_pic = models.ImageField(blank=True, null=True)
    confirmhash = models.CharField(max_length=100, blank=True, null=True)
    
    

    def __str__(self):
        return  self.user.username



class Hospital(models.Model):
	name = models.CharField(max_length=150)
	lat = models.CharField(max_length=100)
	lng = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	profile_pic = models.ImageField(blank=True, null=True)
	def _str_(self):
		return self.lat


class Facility(models.Model):
  name = models.CharField(max_length=150)
  number = models.IntegerField(blank=True)
  description = models.CharField(max_length=300)
  Hosp = models.ForeignKey(Hospital,on_delete=models.CASCADE)
  def _str_(self):
   return self.name


class Doctor(models.Model):
  name = models.CharField(max_length=150)
  phone= models.CharField(max_length=150)
  description = models.CharField(max_length=300)
  availability = models.BooleanField(default='False')
  faci = models.ForeignKey(Facility,on_delete=models.CASCADE)
  def _str_(self):
   return self.name

class Medicine(models.Model):
	faciky = models.ForeignKey(Facility,on_delete=models.CASCADE)
	med_ID = models.CharField(max_length=300)
	Quantity_available = models.IntegerField()
	name_of_med = models.CharField(max_length=200)

class Ward(models.Model):
	Hosp = models.ForeignKey(Hospital,on_delete=models.CASCADE)
	Ward_Availability=models.BooleanField(default='False')
	ward_number = models.CharField(max_length=15)
	floor_number = models.CharField(max_length=5)
'''class Citizen(models.Model):
	name = models.CharField(max_length=150)
	age = models.CharField(max_length=100)
	lat = models.CharField(max_length=100)
	lng = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	gender = models.CharField(max_length=10)
	def _str_(self):
		return self.name	

class Center(models.Model):
	name = models.CharField(max_length=100)
	lat = models.CharField(max_length=100)
	lng = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	vicinity = models.CharField(max_length=100)
	place_id = models.CharField(max_length=100)
	types = models.CharField(max_length=100)
	did = models.CharField(max_length=10)
	typeof = models.CharField(max_length=10)
	def _str_(self):
		return self.name'''
'''class Citizen(models.Model):
	name = models.CharField(max_length=150)
	age = models.CharField(max_length=100)
	lat = models.CharField(max_length=100)
	lng = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	gender = models.CharField(max_length=10)
	def __str__(self):
		return self.name	

class Center(models.Model):
	name = models.CharField(max_length=100)
	lat = models.CharField(max_length=100)
	lng = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	vicinity = models.CharField(max_length=100)
	place_id = models.CharField(max_length=100)
	types = models.CharField(max_length=100)
	did = models.CharField(max_length=10)
	typeof = models.CharField(max_length=10)
	def __str__(self):
		return self.name'''
