from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import ChangeInfoForm

has_ownership=[account_ownership_required, login_required]

def Home(request):
    return render(request, 'base.html')

class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'accountapp/signup.html'

class MypageView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/mypage.html'

    #def get_context_data(self, **kwargs):
    #    object_list = Trainer.objects.filter(writer=self.get_object())
    #    return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class ChangeInfoView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = ChangeInfoForm
    success_url = reverse_lazy('home')
    template_name = 'accountapp/change_info.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
