from django.urls import path
from service import views

app_name = "service"

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("HNsearch", views.HNsearch, name="HNsearch"),

]
