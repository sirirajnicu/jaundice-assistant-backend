from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from service.forms import LoginForm
from django.contrib import messages


class RequestMethod(enumerate):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
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
            messages.error(
                request, "Invalid username or password.", extra_tags="login-error"
            )
        return redirect("service:search", permanent=False)
    else:
        messages.error(request, " ", extra_tags="login")

    return render(request, "views/index.html", context=data)


def search(request: HttpRequest) -> HttpResponse:
    data = {}
    return render(request, "views/search.html", context=data)
