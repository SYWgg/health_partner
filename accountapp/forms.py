from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from accountapp.models import Profile


class ChangeInfoForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
        #auth\forms.py에 있는 UserCreationForm 클래스를 받아와 새로운 클래스인 AccountUpdateForm에서
        #username을 비활성화 시킨 다음 사용한다.

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'image']
