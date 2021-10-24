from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.db import models

# Create your models here.
from accountapp.choice import *


class UserManager(BaseUserManager):
    def create_user(self, user_id, password, email, hp, name, is_trainer, trainer_num, auth, **extra_fields):
        user = self.model(
            user_id=user_id,
            email=email,
            hp=hp,
            name=name,
            is_trainer=is_trainer,
            trainer_num=trainer_num,
            auth=auth,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, email=None, hp=None, name=None, is_trainer=None, trainer_num=None,
                         auth=None):
        user = self.create_user(user_id, password, email, hp, name, is_trainer, trainer_num, auth)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.level = 0
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    user_id = models.CharField(max_length=17, verbose_name="아이디", unique=True)
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    email = models.EmailField(max_length=128, verbose_name="이메일", null=True, unique=True)
    hp = models.IntegerField(verbose_name="핸드폰번호", null=True, unique=True)
    name = models.CharField(max_length=8, verbose_name="이름", null=True)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=18, verbose_name="권한", default=3)
    is_trainer = models.CharField(choices=IS_TRAINER_CHOICES, max_length=24, verbose_name="트레이너/일반인", null=True)
    trainer_num = models.CharField(max_length=20, verbose_name="자격증 번호", null=True)
    auth = models.CharField(max_length=10, verbose_name="인증번호", null=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일', null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "회원목록"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
