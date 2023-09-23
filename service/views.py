from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from service.forms import LoginForm, SearchForm, BabyInfoForm
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
    """
    This view is the index, login, and logout. It will logout user if they already login or serve login page for user.
    """
    if request.user.is_authenticated:
        logout(request)  # ? Somehow we need this place for logout
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


# def logoutUser(request: HttpRequest) -> HttpResponse:
#     #! This code should work but it not
#     logout(request)
#     return redirect("service:loginUser")


@login_required
def HNsearch(request: HttpRequest) -> HttpResponse:
    MockANmap = {"1": [1.1, 1.2, 1.3], "2": [2.1, 2.2], "3": []}  #! testing info
    data = {
        "SearchForm": SearchForm(auto_id=False),
        "pageName": "Create/Search",
    }
    if request.method == RequestMethod.POST:
        form = SearchForm(data=request.POST)
        if form.is_valid():
            searchid = form.cleaned_data["searchid"]
            # TODO implement real thing
            data["HN"] = searchid
            data["ANlist"] = MockANmap[data["HN"]]
            messages.error(request, "Invalid search term.", extra_tags="error")
        else:
            messages.error(request, "Invalid search term.", extra_tags="error")
        return render(request, "views/HNsearch.html", context=data)
    return render(request, "views/HNsearch.html", context=data)

@login_required
def ANsearch(request: HttpRequest) -> HttpResponse:
    if request.method == RequestMethod.POST:
        ANid = request.POST.get("an", default=None)
        if ANid is None:
            messages.error(request, "Invalid search term.", extra_tags="error")
            return redirect("service:HNsearch")
        # TODO implement real thing
        data: dict = {
            "pageName": "ANsearch",
            "ANid": ANid,
        }
        return render(request, "views/ANsearch.html", context=data)
    else:
        return redirect("service:HNsearch")

@login_required
def form(request: HttpRequest) -> HttpResponse:
    data = {
        "BabyInfoForm": BabyInfoForm(auto_id=False),
        "BabyInfo": {"A1":{"firstname":"one", "lastname":"eee","bd":"29/1/2002", "time": "06.00", "bw": "300" , "HN":"A1", "GA": "100", "AN": "111", "admission": "readmit"},
                     "A2":{"firstname":"two", "lastname":"ooo","bd":"1/8/2009", "time": "19.00", "bw": "290" , "HN":"A2", "GA": "120", "AN": "222", "admission": "birth"}},
    }
    if request.method == RequestMethod.POST:
        form = BabyInfoForm(data=request.POST)
        if form.is_valid():
            messages.error(request, "Invalid search term.", extra_tags="error")
        else:
            messages.error(request, "Invalid search term.", extra_tags="error")
        return render(request, "views/form.html", context=data)

    else:
        messages.error(request, " ", extra_tags="error")
    return render(request, "views/form.html", context=data)

