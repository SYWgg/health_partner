from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import MypageView, ChangeInfoView, AccountDeleteView, SignupView

app_name = 'accountapp'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('signup/', SignupView.as_view(), name='signup'),
    path('mypage/<int:pk>', MypageView.as_view(), name='mypage'),
    path('change_info/<int:pk>', ChangeInfoView.as_view(), name='change_info'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]
