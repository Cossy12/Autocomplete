from django.db import models

# Create your models here.


class searchoption(models.Model):
    address = models.TextField()
    
    
    def __str__(self):
        return self.address