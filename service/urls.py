from django.urls import path
from service import views

app_name = "service"

urlpatterns = [
    path("", views.login, name="login"),
    path("logout/", views.login, name="logout"),
    path("HNsearch/", views.HNsearch, name="HNsearch"),
]
