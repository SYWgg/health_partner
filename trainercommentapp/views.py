from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from trainerapp.models import Trainer
from trainercommentapp.decorators import comment_ownership_required
from trainercommentapp.forms import TrainerCommentCreationForm
from trainercommentapp.models import TrainerComment


class TrainerCommentCreateView(CreateView):
    model = TrainerComment
    form_class = TrainerCommentCreationForm
    template_name = 'trainercommentapp/comment_create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.trainer = Trainer.objects.get(id=self.request.POST['trainer_pk'])
        temp_comment.member = self.request.user
        temp_comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('trainerapp:detail', kwargs={'pk': self.object.trainer.pk})





@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class TrainerCommentDeleteView(DeleteView):
    model = TrainerComment
    context_object_name = 'target_comment'
    template_name = 'trainercommentapp/comment_delete.html'

    def get_success_url(self):
        return reverse('trainerapp:detail', kwargs={'pk': self.object.trainer.pk})
