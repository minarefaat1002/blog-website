from asyncio.windows_events import NULL
from email.policy import default
from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=False,upload_to='blog_images')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog-detail',kwargs={'pk':self.pk})