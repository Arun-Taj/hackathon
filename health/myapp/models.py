from django.db import models

# Create your models here.

class Registerform(models.Model):
    user_name=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    img = models.ImageField(upload_to = "images/")

    def __str__(self):
        return self.user_name