from django.db import models
from django.urls import reverse 

# Create your models here.
class Post(models.Model):
    thumbnail = models.ImageField(upload_to='post/photo')
    title = models.CharField(default=None, max_length=200)
    short_description = models.TextField(default=None)
    slug = models.SlugField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Blog:blog_details",kwargs={'slug':self.slug})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='commennts' )
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name