from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.


class About(models.Model):
    headline = models.CharField(max_length=255)
    description = RichTextField()
    fade = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to="media/about/%Y/%m/%d")

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    yt_link = models.CharField(max_length=255, default='some string')
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d")
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name

class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    link = models.CharField(max_length=255,default='SOME STRING')
    photo = models.ImageField(upload_to='media/slider/%Y')
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.headline
    
    
class Services(models.Model):
    headline = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    button_text = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='media/services/%Y/%m')
    description = RichTextField()
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    
    def __str__(self):
        return self.headline 
        