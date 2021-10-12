from django.db import models
from datetime import datetime
# Create your models here.

class Contacttuber(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    tuber_name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250, default="some")
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    
    
    def __str__(self):
        return self.email
    
    
