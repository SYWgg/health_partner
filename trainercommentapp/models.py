from django.db import models

# Create your models here.
from accountapp.models import User
from trainerapp.models import Trainer


class TrainerComment(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, related_name='trainer_comment')
    member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='trainer_comment')

    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now=True)

