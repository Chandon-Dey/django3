from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()
    image = models.ImageField(upload_to='profile\photos')
    created_at = models.DateTimeField(auto_now_add=True)
