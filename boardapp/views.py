from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.db.models import Q
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
    paginate_by = 5



    def get_queryset(self):

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        board_list = Board.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) > 1:
                if search_type == 'all':
                    search_board_list = board_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(
                            writer__user_id__icontains=search_keyword))
                elif search_type == 'title_content':
                    search_board_list = board_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
                elif search_type == 'title':
                    search_board_list = board_list.filter(title__icontains=search_keyword)
                elif search_type == 'content':
                    search_board_list = board_list.filter(content__icontains=search_keyword)

                return search_board_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return board_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')

        if len(search_keyword) > 1:
            context['q'] = search_keyword
        context['type'] = search_type

        return context




