from django.conf.urls import url
from django.urls import path
from loginApp import views

urlpatterns = [
    url(r'^$', views.login, name="login"),
    path("login", views.login, name="login"),
]