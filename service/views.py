from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from service.forms import LoginForm, SearchForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as authlogin
from django.contrib.auth import logout as authlogout
from django.contrib.auth.decorators import login_required


class RequestMethod(enumerate):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


# Create your views here.
def login(request: HttpRequest) -> HttpResponse:
    data = {
        "LoginForm": LoginForm(auto_id=False),
    }
    if request.method == RequestMethod.POST:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username: str = form.cleaned_data["username"]
            password: str = form.cleaned_data["password"]
            role: str = form.cleaned_data["role"]
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                authlogin(request, user)
                request.session["role"] = role
                return redirect("service:HNsearch")
        else:
            messages.error(request, "Invalid username or password.", extra_tags="error")
    else:
        messages.error(request, " ", extra_tags="error")
    return render(request, "views/index.html", context=data)


@login_required
def logout(request: HttpRequest) -> HttpResponse:
    authlogout(request)
    return redirect("/")


@login_required
def HNsearch(request: HttpRequest) -> HttpResponse:
    data = {
        "SearchForm": SearchForm(auto_id=False),
    }
    if request.method == RequestMethod.POST:
        form = SearchForm(data=request.POST)
        if form.is_valid():
            searchid = form.cleaned_data["searchid"]
            data["HN"] = searchid
            messages.error(request, "Invalid search term.", extra_tags="error")

        else:
            messages.error(request, "Invalid search term.", extra_tags="error")
        return render(request, "views/HNsearch.html", context=data)

    else:
        messages.error(request, " ", extra_tags="error")
    return render(request, "views/HNsearch.html", context=data)
