"""Define urls for user package"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, path, include
from django.contrib.auth import views as auth_views

from . import views
from .views import RegisterView, CustomLoginView, ResetPasswordView, profile, ChangePasswordView
from .forms import LoginForm

app_name = 'user'


urlpatterns =[
    path('', views.home, name="users-home"),
    path('register/', RegisterView.as_view(), name="users-register"),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True,
    template_name='auth/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'),
    name='password_reset_confirm'),
    path('password-reset-complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'),
    name='password_reset_complete'),
    path('profile/', profile, name='users-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
