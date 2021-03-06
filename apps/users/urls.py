from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views as user_view

from .forms import CustomPasswordReset

app_name = 'users'

urlpatterns = [
    path('', user_view.register, name="register"),
    path('register/', user_view.register, name="register"),
    path('home/', user_view.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='users/register/password_reset.html',
        email_template_name='users/register/password_reset_email.html',
        success_url='/users/reset_password_done',
        form_class=CustomPasswordReset),
        name="password_reset"
    ),
    path('reset_password_done', auth_views.PasswordResetDoneView.as_view(
        template_name='users/register/password_reset_done.html'),
        name="password_reset_done"
    ),
    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/register/password_reset_confirm.html',
        success_url='/password_reset_complete/'),
        name='password_reset_confirm'
 ),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/register/password_reset_complete.html'),
        name='password_reset_complete'
    ),
    url('activate/(?P<uidb64>[0-9A-Za-z\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        user_view.activate, name='activate'
    ),
]
