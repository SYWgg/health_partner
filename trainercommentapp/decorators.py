
from django.http import HttpResponseForbidden

from commentapp.models import Comment
from trainercommentapp.models import TrainerComment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = TrainerComment.objects.get(pk=kwargs['pk'])
        if not comment.member == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
