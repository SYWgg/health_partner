from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Board(models.Model):
    writer = models.OneToOneField(User, related_name='question', on_delete=models.CASCADE, verbose_name='작성자')

    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(upload_to='board/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="최종수정일")

    class Meta:
        db_table = 'board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'

    def __str__(self):
        return self.title
