from django.urls import path

from service import views

app_name = "service"

urlpatterns = [
    path("", views.loginUser, name="loginUser"),
    path("login/", views.loginUser, name="loginUser"),
    path("HNsearch/", views.HNsearch, name="HNsearch"),
]
