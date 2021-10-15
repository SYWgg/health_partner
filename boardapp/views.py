from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView

from boardapp.decorators import board_ownership_required
from boardapp.forms import BoardCreationForm
from boardapp.models import Board
from commentapp.forms import CommentCreationForm

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class BoardCreateView(CreateView):
    model = Board
    form_class = BoardCreationForm
    template_name = 'boardapp/board_create.html'

    def form_valid(self, form):
        temp_board = form.save(commit=False)
        temp_board.writer = self.request.user
        temp_board.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('boardapp:detail', kwargs={'pk': self.object.pk})

class BoardDetailView(DetailView, FormMixin):
    model = Board
    form_class = CommentCreationForm
    context_object_name = 'target_board'
    template_name = 'boardapp/board_detail.html'


@method_decorator(board_ownership_required, 'get')
@method_decorator(board_ownership_required, 'post')
class BoardUpdateView(UpdateView):
    model = Board
    form_class = BoardCreationForm
    context_object_name = 'target_board'
    template_name = 'boardapp/board_update.html'

    def get_success_url(self):
        return reverse('boardapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(board_ownership_required, 'get')
@method_decorator(board_ownership_required, 'post')
class BoardDeleteView(DeleteView):
    model = Board
    context_object_name = 'target_board'
    success_url = reverse_lazy('boardapp:list')
    template_name = 'boardapp/board_delete.html'

class BoardListView(ListView):
    model = Board
    context_object_name = 'board_list'
    template_name = 'boardapp/board_list.html'
    paginate_by = 10
