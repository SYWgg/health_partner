from django.db import models

# Create your models here.

class Video(models.Model):

    title = models.CharField(max_length=100,verbose_name="유튜브 제목")
    url = models.URLField(verbose_name="유튜브 url")