from django.db import models


# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=20, unique=True, null=True)
    full_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'