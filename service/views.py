from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from service.forms import LoginForm, SearchForm


class RequestMethod(enumerate):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


# Create your views here.
def loginUser(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        logout(request)
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
            print(user, password, role)
            if user is not None:
                login(request, user)
                request.session["role"] = role
                request.session.get_expire_at_browser_close()
                return redirect("service:HNsearch", permanent=False)
            else:
                messages.error(
                    request, "Invalid username or password.", extra_tags="error"
                )
        else:
            messages.error(request, "Invalid username or password.", extra_tags="error")
    return render(request, "views/index.html", context=data)


@login_required
def HNsearch(request: HttpRequest) -> HttpResponse:
    MockANmap = {"1": [1.1, 1.2, 1.3], "2": [2.1, 2.2], "3": []}
    data = {
        "SearchForm": SearchForm(auto_id=False),
        "pageName": "Create/Search",
    }
    if request.method == RequestMethod.POST:
        form = SearchForm(data=request.POST)
        if form.is_valid():
            searchid = form.cleaned_data["searchid"]
            data["HN"] = searchid
            data["ANlist"] = MockANmap[data["HN"]]
            messages.error(request, "Invalid search term.", extra_tags="error")
        else:
            messages.error(request, "Invalid search term.", extra_tags="error")
        return render(request, "views/HNsearch.html", context=data)
    return render(request, "views/HNsearch.html", context=data)


def ANsearch(request: HttpRequest) -> HttpResponse:
    data: dict = {
        "pageName": "ANsearch",
    }
    if request.method != RequestMethod.POST:
        return redirect("service:HNsearch")
    return render(request, "views/ANsearch.html", context=data)
