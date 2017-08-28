from django.db import models
from .validators import *
class ContactInfo(models.Model):
    mobile_number = models.CharField(max_length=15, validators=[validate_mobile_no])
    phone_number = models.CharField(max_length=15, validators=[validate_phone_no])
    email_id = models.EmailField()
class Address(models.Model):
    address_id= models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True,null=True, validators=[validate_city])
    state= models.CharField(max_length=20, blank=True, null=True, validators=[validate_state])
    landmark= models.CharField(max_length=20, blank=True, null=True, validators=[validate_landmark])
    pincode= models.IntegerField(blank=True, null=True)
class Customer(ContactInfo):
    customer_id= models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    address= models.ManyToManyField("Address",blank=True,null=True)

class Agent(ContactInfo):
    agent_id= models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=20,validators=[validate_first_name])
    last_name= models.CharField(max_length=20,validators=[validate_last_name])
    age=models.IntegerField()
    education= models.CharField(max_length=50,validators=[validate_education])
    company_name=models.CharField(max_length=50)
    specialization= models.CharField(max_length=100,validators=[validate_specelization])
    experence=models.IntegerField()
    agent_notes=models.TextField()
    address = models.ManyToManyField("Address")