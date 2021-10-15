from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from boardapp.models import Board
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/comment_create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.board = Board.objects.get(pk=self.request.POST['board_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('boardapp:detail', kwargs={'pk': self.object.board.pk})


@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/comment_delete.html'

    def get_success_url(self):
        return reverse('boardapp:detail', kwargs={'pk': self.object.board.pk})
