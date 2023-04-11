from django.db import models
from customer.models import Customer
from office.models import Office
from twilio.rest import Client
import random


class Visitor(models.Model):
    company  = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    id_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.CharField(max_length=200, null=True, blank=True)
    visited_from = models.CharField(max_length=200, null=True, blank=True)
    phone= models.CharField(max_length=200, null=True, blank=True)
    office_visited_phone= models.CharField(max_length=200, null=True, blank=True)
    is_signed_out = models.BooleanField(default=0, null=True)
    sign_out_code = models.CharField(max_length=6, null=True, blank=True, unique=True)
    time_in = models.TimeField(auto_now_add=True, null=True)
    time_out = models.TimeField(null=True, blank=True)
    date_visited = models.DateField(auto_now=True, null=True, blank=True)
    office_visited = models.CharField(max_length=200, null=True, blank=True)
    on_behalf = models.CharField(max_length=200, null=True, blank=True)



  
    def __str__(self):
        return self.first_name+' '+self.last_name


    # def save(self, *args, **kwargs):
    #     account_sid = "AC7de809070e43f0f3038d7110b322c5ff"
    #     auth_token = "986557a5e258d10500750c069b15c993"
    #     client = Client(account_sid, auth_token)
    #     office_notify = client.messages.create(
    #     body="Hellow, you have a visitor"+' '+self.first_name +' '+self.middle_name,
    #     from_="+15855801079",
    #     to = self.office_visited_phone
    #     )

    #     visitor_sign_out = client.messages.create(
    #     body="Hellow welcome"+' '+self.office_visited+' '+"Your sign out code is "+self.sign_out_code+", please do not delete this massage until you signed out, use code during getting out",
    #     from_="+15855801079",
    #     to=self.phone
        
    #     )
    #     print(visitor_sign_out.sid)
    #     print(office_notify.sid)
    #     return super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        self.sign_out_code = random.randint(1000, 9999)
        return super().save(*args, **kwargs)