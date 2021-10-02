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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    # on_delete => 연결된 User이 없어질때 CASECADE된다.(사라진다)

    image = models.ImageField(upload_to='image/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
