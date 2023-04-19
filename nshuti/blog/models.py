from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images', null=True, blank=True)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

