# Generated by Django 3.2.7 on 2021-10-14 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='트레이너 이름')),
                ('img', models.ImageField(upload_to='trainer/', verbose_name='트레이너 사진')),
                ('trainer_intro', models.TextField(verbose_name='트레이너 소개')),
                ('program_intro', models.TextField(verbose_name='프로그램 소개')),
                ('charge', models.CharField(max_length=100, verbose_name='트레이닝 가격')),
                ('training_time', models.CharField(max_length=100, verbose_name='트레이닝 시간표')),
                ('career', models.TextField(verbose_name='트레이너 경력')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='최종수정일')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='트레이너')),
            ],
        ),
    ]
