# Generated by Django 3.2.7 on 2021-10-31 08:46

from django.db import migrations, models
import embed_video.fields


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
                ('tags', models.CharField(blank=True, max_length=100, null=True, verbose_name='유튜브 조회수')),
                ('url', embed_video.fields.EmbedVideoField()),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='조회수')),
            ],
        ),
    ]
