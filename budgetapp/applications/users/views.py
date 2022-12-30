"""
Django views
"""
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import NewUserForm
from .utils import HttpResponseHXRedirect


@require_http_methods(["GET", "POST"])
def register_request(request: HttpRequest) -> HttpResponse:
    """Render register page and create new user"""
    template = "registration/register.html"

    if request.method == "GET":
        form = NewUserForm()
        context = {"form": form}
        return TemplateResponse(request, template=template, context=context)

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("budget:home")
        messages.error(
            request, "Unsuccessful registration. Invalid information."
        )
        print(form.errors)
        context = {"form": form}
        return TemplateResponse(request, template=template, context=context)


@require_http_methods(["GET", "POST"])
def login_request(request: HttpRequest) -> HttpResponse:
    """Render the login page and authenticates the user"""
    template = "registration/login.html"

    if request.method == "GET":
        form = AuthenticationForm()
        context = {"form": form}
        return TemplateResponse(request, template=template, context=context)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect("budget:home")
            else:
                messages.error(request, "Invalid username or password.")
                return HttpResponseHXRedirect(
                    redirect_to=reverse_lazy("users:login")
                )
        else:
            messages.error(request, "Invalid username or password.")
            return HttpResponseHXRedirect(
                redirect_to=reverse_lazy("users:login")
            )
