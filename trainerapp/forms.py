from django.forms import ModelForm

from trainerapp.models import Trainer


class TrainerCreationForm(ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'img', 'trainer_intro', 'program_intro', 'charge', 'training_time', 'career']
