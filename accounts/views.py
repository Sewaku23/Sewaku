from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm


def home(request):
    return render(request, "home.html")


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("home")

    else:

        form = RegisterForm()

    return render(request, "accounts/register.html", {
        "form": form
    })


def user_login(request):

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            login(request, form.get_user())

            return redirect("home")

    else:

        form = LoginForm()

    return render(request, "accounts/login.html", {
        "form": form
    })


def user_logout(request):

    logout(request)

    return redirect("home")


@login_required
def profile(request):

    return render(request, "accounts/profile.html")