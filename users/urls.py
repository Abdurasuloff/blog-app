from django.urls import path
from .views import signup
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", signup, name="signup"),
    
    path("password-change/", PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path("password-change-done/", PasswordChangeDoneView.as_view(template_name='registration/password_done.html'), name='password_change_done'),
    
    path("password-reset/", PasswordResetView.as_view(template_name="registration/pass_reset.html"), name='password_reset'),
    path("password-reset/done/", PasswordResetDoneView.as_view(template_name="registration/pass_reset_done.html"), name="password_reset_done"),
    path("password-reset/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name="registration/pass_confirm.html"), name="password_reset_confirm"),
    path("password-reset/complete/", PasswordResetCompleteView.as_view(template_name="registration/pass_reset_complete.html"), name="password_reset_complete"),
]
