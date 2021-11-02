from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from accountapp.decorators import trainer_required
from commentapp.forms import CommentCreationForm
from trainerapp.decorators import trainer_ownership_required
from trainerapp.forms import TrainerCreationForm
from trainerapp.models import Trainer, RegisteredUser
from trainercommentapp.forms import TrainerCommentCreationForm


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(trainer_required, name='dispatch')
class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerCreationForm
    template_name = 'trainerapp/trainer_create.html'
    def form_valid(self, form):
        temp_trainer = form.save(commit=False)
        temp_trainer.trainer = self.request.user
        temp_trainer.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('trainerapp:detail', kwargs={'pk': self.object.pk})


class TrainerDetailView(DetailView):
    model = Trainer
    context_object_name = 'target_trainer'
    template_name = 'trainerapp/trainer_detail.html'

@method_decorator(trainer_ownership_required, 'get')
@method_decorator(trainer_ownership_required, 'post')
@method_decorator(trainer_required, name='dispatch')
class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerCreationForm
    context_object_name = 'target_trainer'
    template_name = 'trainerapp/trainer_update.html'

    def get_success_url(self):
        return reverse('trainerapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(trainer_ownership_required, 'get')
@method_decorator(trainer_ownership_required, 'post')
@method_decorator(trainer_required, name='dispatch')
class TrainerDeleteView(DeleteView):
    model = Trainer
    context_object_name = 'target_trainer'
    success_url = reverse_lazy('trainerapp:list')
    template_name = 'trainerapp/trainer_delete.html'


class TrainerListView(ListView):
    model = Trainer
    context_object_name = 'trainer_list'
    template_name = 'trainerapp/trainer_list.html'
    paginate_by = 8

    def get_queryset(self):

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        trainer_list = Trainer.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) >= 1:
                if search_type == 'all':
                    search_trainer_list = trainer_list.filter(
                        Q(name__icontains=search_keyword) | Q(trainer_intro__icontains=search_keyword) | Q(
                            program_intro__icontains=search_keyword))
                elif search_type == 'name':
                    search_trainer_list = trainer_list.filter(name__icontains=search_keyword)
                elif search_type == 'trainer_intro':
                    search_trainer_list = trainer_list.filter(trainer_intro__icontains=search_keyword)
                elif search_type == 'program_intro':
                    search_trainer_list = trainer_list.filter(program_intro__icontains=search_keyword)

                return search_trainer_list
            else:
                messages.error(self.request, '검색어는 1글자 이상 입력해주세요.')
        return trainer_list

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

class InquiredBoardView(DetailView, FormMixin):
    model = Trainer
    context_object_name = 'target_trainer'
    template_name = 'trainerapp/inquired_board.html'
    form_class = TrainerCommentCreationForm
