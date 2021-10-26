from django import forms
from django.forms import ModelForm

from boardapp.models import Board


class BoardCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BoardCreationForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })

    class Meta:
        model = Board
        fields = ['title', 'content', 'image']
