from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class BgyResident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    philhealth = models.CharField(max_length=20)
    highest_education = models.CharField(max_length=20)
    remarks = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=20, blank=True)
    file_upload = models.FileField(upload_to='resident/%Y/%m/%d/')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date_published = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name