from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from service.forms import LoginForm, SearchForm
from django.contrib import messages


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
            # if True:
            #     return redirect("service:search", permanent=False)
            # else:
            #     messages.error(
            #         request, "Invalid username or password.", extra_tags="login-error"
            #     )
        else:
            messages.error(request, "Invalid username or password.", extra_tags="error")
        return redirect("service:search", permanent=False)
    else:
        messages.error(request, " ", extra_tags="error")

    return render(request, "views/index.html", context=data)


def logout(request: HttpRequest) -> HttpResponse:
    # logic here
    return redirect("service:logout", permanent=False)


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
