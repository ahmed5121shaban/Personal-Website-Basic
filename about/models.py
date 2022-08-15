from django.db import models

# Create your models here.
class About(models.Model):
    about_name = models.CharField(max_length=100)
    about_me = models.CharField(max_length=10000)
    imag = models.ImageField(upload_to='about/%y/%m/%d')
    subtitle = models.TextField(max_length=500)
    tw_link = models.URLField()
    git_link = models.URLField()
    in_link = models.URLField()


    def __str__(self) -> str:
        return self.about_name
