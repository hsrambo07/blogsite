from django.db import models


class page(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    summary=models.CharField(max_length=200)

    image = models.ImageField(upload_to='images/')
    
