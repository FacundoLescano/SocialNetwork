from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="basic"
urlpatterns = [
    #path('error/s', auth_views.LoginView.as_view()),
    path("", views.index, name="index"),
    path("presentation/", views.presentation, name="presentation"),
    path("signup/", views.signUp, name="signUp"),
    path("response/", views.response, name="response"),
    path("profile/", views.profile, name="profile"),
    path("error-401/", views.error_401, name="error"),
    path("login/", views.user_login, name="login"),
    path("response-login/", views.response_login, name="response-login")
]