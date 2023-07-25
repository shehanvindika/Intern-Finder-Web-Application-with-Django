from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.logIn),
    path('vacancies', views.vacancy),
    path('createpost', views.createPost),
    path('register', views.register),
    path('profile', views.profile),
    path('apply', views.sendEmails),
]