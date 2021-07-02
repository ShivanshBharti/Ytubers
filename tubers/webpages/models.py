from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=250)
    subtitle= models.CharField(max_length=250)
    button_text = models.CharField(max_length=250)
    photo = models.ImageField(upload_to = 'media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.headline

class Team(models.Model):
    first_name= models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    role= models.CharField(max_length=250)
    photo= models.ImageField(upload_to = 'media/team/%Y/%m/%d')
    fb_link = models.CharField(max_length=250)
    insta_link = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    youtube_link = models.CharField(max_length=250,default="")


    
    def __str__(self):
        return self.first_name

class About(models.Model):
    Description = RichTextField()
    photo= models.ImageField(upload_to = 'media/about/%Y/%m/%d')

    def __str__(self):
        return self.Description
        