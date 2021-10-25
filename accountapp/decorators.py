# from django.contrib.auth.models import User
# from django.http import HttpResponseForbidden
#
#
# def account_ownership_required(func):
#     def decorated(request, *args, **kwargs):
#         user = User.objects.get(pk=kwargs['pk'])
#         if not user == request.user:
#             return HttpResponseForbidden()
#         return func(request, *args, **kwargs)
#
#     return decorated


# 로그인 확인
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect

from accountapp.models import User


def login_message_required(function):
    def decorated(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "로그인한 사용자만 이용할 수 있습니다.")
            return redirect(settings.LOGIN_URL)
        return function(request, *args, **kwargs)

    return decorated


# 트레이너 권한 확인
def trainer_required(function):
    def decorated(request, *args, **kwargs):
        if request.user.level == '2' or request.user.level == '1' or request.user.level == '0':
            return function(request, *args, **kwargs)
        messages.info(request, "접근 권한이 없습니다.")
        return redirect('home')

    return decorated


# 비로그인 확인
def logout_message_required(function):
    def decorated(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "접속중인 사용자입니다.")
            return redirect('home')
        return function(request, *args, **kwargs)

    return decorated
