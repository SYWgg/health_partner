from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, FormView, DetailView

from accountapp.decorators import logout_message_required, login_message_required
from accountapp.forms import TrainerRegisterForm, LoginForm, RegisterForm, CustomPasswordChangeForm, CheckPasswordForm
from accountapp.models import User


@method_decorator(logout_message_required, name='dispatch')
class LoginView(FormView):
    template_name = 'accountapp/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=user_id, password=password)

        if user is not None:
            self.request.session['user_id'] = user_id
            login(self.request, user)

        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('/')


@method_decorator(logout_message_required, name='dispatch')
class AgreementView(View):
    def get(self, request, *args, **kwargs):
        request.session['agreement'] = False
        return render(request, 'accountapp/agreement.html')

    def post(self, request, *args, **kwarg):
        if request.POST.get('agreement1', False) and request.POST.get('agreement2', False):
            request.session['agreement'] = True

            if request.POST.get('trainer_register') == 'trainer_register':
                return redirect('/accounts/trainer_register/')
            else:
                return redirect('/accounts/register/')
        else:
            messages.info(request, "약관에 모두 동의해주세요.")
            return render(request, 'accountapp/agreement.html')


class TrainerRegisterView(CreateView):
    model = User
    template_name = 'accountapp/trainer_register.html'
    form_class = TrainerRegisterForm

    def get(self, request, *args, **kwargs):
        if not request.session.get('agreement', False):
            raise PermissionDenied
        request.session['agreement'] = False

        url = settings.LOGIN_REDIRECT_URL
        if request.user.is_authenticated:
            return HttpResponseRedirect(url)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, "회원가입 성공.")
        return reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())


class RegisterView(CreateView):
    model = User
    template_name = 'accountapp/register.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        if not request.session.get('agreement', False):
            raise PermissionDenied
        request.session['agreement'] = False

        url = settings.LOGIN_REDIRECT_URL
        if request.user.is_authenticated:
            return HttpResponseRedirect(url)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, "회원가입 성공.")
        return reverse_lazy('home')

    def form_valid(self, form):
        self.objects = form.save()
        return redirect(self.get_success_url())


@login_message_required
def password_update_view(request):
    if request.method == 'POST':
        password_change_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            # logout(request)
            messages.success(request, "비밀번호를 성공적으로 변경하였습니다.")
            return redirect('/')
    else:
        password_change_form = CustomPasswordChangeForm(request.user)

    return render(request, 'accountapp/password_update.html', {'password_change_form': password_change_form})


@login_message_required
def account_delete_view(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('/accounts/login/')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'accountapp/account_delete.html', {'password_form': password_form})


class MypageView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/mypage.html'

    # def get_context_data(self, **kwargs):
    #    object_list = Trainer.objects.filter(writer=self.get_object())
    #    return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

