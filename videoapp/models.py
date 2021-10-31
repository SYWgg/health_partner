from django.db import models

# Create your models here.
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    title = models.CharField(max_length=50, verbose_name="영상 제목")
    tags = models.CharField(max_length=100, null=True, blank=True, verbose_name="유튜브 조회수")
    url = EmbedVideoField()

    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()
