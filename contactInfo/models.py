from django.db import models
from datetime import datetime
from phone_field import PhoneField

# Create your models here.

class ContactInfo(models.Model):
    email = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    add = models.TextField(blank=True)
    insta_link = models.CharField(max_length=255)
    tw_link = models.CharField(max_length=255)
    yt_link = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    
                               
                               
                               
                               
            
    
