from django.forms import ModelForm

from trainercommentapp.models import TrainerComment


class TrainerCommentCreationForm(ModelForm):
    class Meta:
        model = TrainerComment
        fields = ['content']