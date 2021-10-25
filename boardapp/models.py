from django.conf import settings
from django.db import models


# Create your models here.
from accountapp.models import User


class Board(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')

    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(upload_to='board/', null=True, blank=True)
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="최종수정일")

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Q&A게시판'
        verbose_name = 'Q&A게시판'
        verbose_name_plural = 'Q&A게시판'