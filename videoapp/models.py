from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=50, verbose_name="영상 제목")
    url = models.CharField(max_length=100, verbose_name="영상 주소")
    views = models.CharField(max_length=100, verbose_name="조회수")
    tag = models.CharField(max_length=100, verbose_name="태그")

