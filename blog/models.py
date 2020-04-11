from django.db import models

# Create your models here.

class BLOG(models.Model):
    title=models.CharField(max_length=20)
    pub_date=models.DateTimeField()
    summary=models.CharField(max_length=20)
    body=models.TextField()
    image=models.ImageField(upload_to='image/')
    