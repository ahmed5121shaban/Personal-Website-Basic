from tkinter import Image
from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100000)
    image = models.ImageField(upload_to='post/%y/%m/%d')
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title