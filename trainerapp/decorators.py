from django.http import HttpResponseForbidden

from trainerapp.models import Trainer


def trainer_ownership_required(func):
    def decorated(request, *args, **kwargs):
        trainer = Trainer.objects.get(pk=kwargs['pk'])
        if not trainer.trainer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
