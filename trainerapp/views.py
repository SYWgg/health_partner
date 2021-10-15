from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from trainerapp.decorators import trainer_ownership_required
from trainerapp.forms import TrainerCreationForm
from trainerapp.models import Trainer


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
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
class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerCreationForm
    context_object_name = 'target_trainer'
    template_name = 'trainerapp/trainer_update.html'

    def get_success_url(self):
        return reverse('trainerapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(trainer_ownership_required, 'get')
@method_decorator(trainer_ownership_required, 'post')
class TrainerDeleteView(DeleteView):
    model = Trainer
    context_object_name = 'target_trainer'
    success_url = reverse_lazy('trainerapp:list')
    template_name = 'trainerapp/trainer_delete.html'

class TrainerListView(ListView):
    model = Trainer
    context_object_name = 'Trainer_list'
    template_name = 'trainerapp/trainer_list.html'
    paginate_by = 8
