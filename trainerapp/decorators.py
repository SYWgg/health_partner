from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

from trainerapp.models import Trainer


def trainer_ownership_required(func):
    def decorated(request, *args, **kwargs):
        trainer = Trainer.objects.get(pk=kwargs['pk'])
        if not trainer.trainer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated

def login_message_required(function):
    def decorated(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "로그인한 사용자만 이용할 수 있습니다.")
            return redirect(settings.LOGIN_URL)
        return function(request, *args, **kwargs)

    return decorated