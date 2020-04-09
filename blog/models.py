from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=50)
    pub_date=models.DateTimeField()
    body= models.TextField()
    summary=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')
    
