from django import forms
from django.forms import ModelForm

from boardapp.models import Board


class BoardCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'height:auto; text-align: left'}))

    class Meta:
        model = Board
        fields = ['title', 'content', 'image']