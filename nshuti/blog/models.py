from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


from tinymce.models import HTMLField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images', null=True, blank=True)
    content = HTMLField('Content')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

