from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.hashers import check_password

from accountapp.choice import *
from .models import User


def hp_validator(value):
    if len(str(value)) != 10:
        raise forms.ValidationError('정확한 핸드폰 번호를 입력해주세요.')


# 로그인 폼
class LoginForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', }),
        error_messages={
            'required': '아이디을 입력해주세요.'
        },
        max_length=32,
        label='아이디'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', }),
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')
        password = cleaned_data.get('password')

        if user_id and password:
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                self.add_error('user_id', '아이디가 존재하지 않습니다.')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')


# 일반회원정보 수정 폼
class CustomUserChangeForm(UserChangeForm):
    password = None
    hp = forms.IntegerField(label='연락처', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'maxlength': '11', 'oninput': "maxLengthCheck(this)", }),
                            )
    name = forms.CharField(label='이름', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength': '8', }),
                           )
    is_trainer = forms.ChoiceField(choices=IS_TRAINER_CHOICES, label='트레이너/일반인', widget=forms.Select(
        attrs={'class': 'form-control', }),
                                   )

    class Meta:
        model = get_user_model()
        fields = ['hp', 'name', 'is_trainer']


# 트레이너 회원정보 수정 폼
class CustomTrainerChangeForm(UserChangeForm):
    password = None
    hp = forms.IntegerField(label='연락처', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'maxlength': '11', 'oninput': "maxLengthCheck(this)", }),
                            )
    name = forms.CharField(label='이름', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength': '8', }),
                           )
    is_trainer = forms.ChoiceField(choices=IS_TRAINER_CHOICES, label='트레이너/일반인', widget=forms.Select(
        attrs={'class': 'form-control', }),
                                   )
    trainer_num = forms.ChoiceField(label='자격증번호', widget=forms.Select(
        attrs={'class': 'form-control', }),
                                    )

    class Meta:
        model = get_user_model()
        fields = ['hp', 'name', 'is_trainer', 'trainer_num']


# 회원탈퇴 비밀번호확인 폼
class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control', }),
                               )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')



# 비밀번호 변경 폼
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = '기존 비밀번호'
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'autofocus': False,
            'style': 'margin-top:-15px;'
        })
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })


# 트레이너 회원가입 폼
class TrainerRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(TrainerRegisterForm, self).__init__(*args, **kwargs)

        self.fields['user_id'].label = '아이디'
        self.fields['user_id'].widget.attrs.update({
            # 'class': 'form-control col-sm-10',
            'class': 'form-control',
            # 'placeholder': '아이디를 입력해주세요.',
            'autofocus': False
        })
        self.fields['password1'].label = '비밀번호'
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': '비밀번호를 입력해주세요.',
        })
        self.fields['password2'].label = '비밀번호 확인'
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': '비밀번호를 다시 입력해주세요.',
        })
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': '회원가입 후 입력하신 메일로 본인인증 메일이 전송됩니다.',
        })
        self.fields['name'].label = '이름'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': "아이디, 비밀번호 찾기에 이용됩니다.",
        })
        self.fields['hp'].label = '핸드폰번호'
        self.fields['hp'].validators = [hp_validator]
        self.fields['hp'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': "'-'를 제외한 숫자로 입력해주세요",
        })
        self.fields['trainer_num'].label = '자격증번호'
        self.fields['trainer_num'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': "트레이너 자격증 번호를 입력해주세요",
        })

    class Meta:
        model = User
        fields = ['user_id', 'password1', 'password2', 'email', 'name', 'hp', 'trainer_num']

    def save(self, commit=True):
        user = super(TrainerRegisterForm, self).save(commit=False)
        user.level = '2'
        user.is_trainer = '트레이너'
        user.save()

        return user


# 일반인 회원가입 폼
class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['user_id'].label = '아이디'
        self.fields['user_id'].widget.attrs.update({
            # 'class': 'form-control col-sm-10',
            'class': 'form-control',
            'autofocus': False,
            # 'placeholder': '아이디를 입력해주세요.',
        })
        self.fields['password1'].label = '비밀번호'
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': '비밀번호를 입력해주세요.',
        })
        self.fields['password2'].label = '비밀번호 확인'
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': '비밀번호를 다시 입력해주세요.',
        })
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['name'].label = '이름'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['hp'].label = '핸드폰번호'
        self.fields['hp'].validators = [hp_validator]
        self.fields['hp'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': "'-'를 제외한 숫자로 입력해주세요",
        })

    class Meta:
        model = User
        fields = ['user_id', 'password1', 'password2', 'email', 'name', 'hp']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.level = '3'
        user.is_trainer = '일반인'
        user.save()

        return user
