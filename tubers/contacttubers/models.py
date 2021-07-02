from django.db import models
from datetime import datetime
# Create your models here.
class Contacttuber(models.Model):
    full_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField(blank=True)
    #user_id=models.IntegerField()
    created_date=models.DateTimeField(blank=True,default=datetime.now)

    def __str__(self):
        return self.full_name