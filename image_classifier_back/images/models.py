from django.db import models

# Create your models here.
class Image(models.Model):
    picture = models.ImageField()
    classfied = models.CharField(max_length=200, blank = True)
    upload_date = models.DateTimeField(auto_now_add=True)
    