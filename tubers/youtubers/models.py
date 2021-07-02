from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):
    crew_choice = (
        ('solo','solo'),
        ('small crew','small crew'),
        ('large crew','large crew'),
    )

    camera_choice = (
        ('sony','sony'),
        ('canon','canon'),
        ('nikon','nikon'),
        ('fuji','fuji'),

    )

    category_choice = (
        ('music','music'),
        ('education','education'),
        ('sports','sports'),
        ('cooking','cooking'),
        ('gaming','gaming'),
        ('vlogs','vlogs'),
        ('comedy','comedy'),


    )


    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()
    role = models.CharField(max_length=250)
    price = models.IntegerField()
    photo= models.ImageField(upload_to = 'media/ytubers/%Y/%m')
    city = models.CharField(max_length=250)
    subs = models.IntegerField(default="0")
    Description = RichTextField()
    fb_link = models.CharField(max_length=250)
    insta_link = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=datetime.now,blank=True)
    youtube_link = models.CharField(max_length=250,default="")
    crew = models.CharField(choices= crew_choice, max_length=250, default="")
    camera = models.CharField(choices= camera_choice, max_length=250, default="")
    category = models.CharField(choices=category_choice, max_length=250,default="")
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name