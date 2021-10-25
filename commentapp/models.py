from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from accountapp.models import User
from boardapp.models import Board


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')

    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now=True)
