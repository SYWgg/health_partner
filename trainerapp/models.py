from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Trainer(models.Model):
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='트레이너')

    name = models.CharField(max_length=10, verbose_name="트레이너 이름")
    img = models.ImageField(upload_to='trainer/', null=False, verbose_name="트레이너 사진")
    trainer_intro = models.TextField(null=False, verbose_name="트레이너 소개")
    program_intro = models.TextField(null=False, verbose_name="프로그램 소개")
    charge = models.CharField(max_length=100, verbose_name="트레이닝 가격")
    training_time = models.CharField(max_length=100, verbose_name="트레이닝 시간표")
    career = models.TextField(null=False, verbose_name="트레이너 경력")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="최종수정일")
