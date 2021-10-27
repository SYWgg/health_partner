# Generated by Django 3.2.7 on 2021-10-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='영상 제목')),
                ('url', models.CharField(max_length=100, verbose_name='영상 주소')),
                ('views', models.CharField(max_length=100, verbose_name='조회수')),
                ('tag', models.CharField(max_length=100, verbose_name='태그')),
            ],
        ),
    ]