from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp import views
from accountapp.views import MypageView

app_name = 'accountapp'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('mypage/<int:pk>', MypageView.as_view(), name='mypage'),
    path('agreement/', views.AgreementView.as_view(), name='agreement'),
    path('trainer_register/', views.TrainerRegisterView.as_view(), name='trainer_register'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('update/', views.password_update_view, name='password_update'),
    path('delete/', views.account_delete_view, name='account_delete'),
]