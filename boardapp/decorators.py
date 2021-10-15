
from django.http import HttpResponseForbidden

from boardapp.models import Board


def board_ownership_required(func):
    def decorated(request, *args, **kwargs):
        board = Board.objects.get(pk=kwargs['pk'])
        if not board.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated