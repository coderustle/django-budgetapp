"""
Django views
"""
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods

from .forms import NewUserForm
from .utils import HttpResponseHXRedirect


@require_http_methods(["GET", "POST"])
def register_request(request: HttpRequest) -> HttpResponse:
    """Render register page and create new user"""
    if request.htmx:
        template = "registration/partials/register.html"
    else:
        template = "registration/register.html"

    if request.method == "GET":
        form = NewUserForm()
        context = {"form": form}
        return TemplateResponse(request, template=template, context=context)

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user, backend=backend)
            messages.success(request, "Registration successful.")
            return redirect("budget:home")
        if form.errors:
            messages.error(request,str(form.errors))
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
        context = {"form": form}
        return TemplateResponse(request, template=template, context=context)
    return HttpResponse(status_code=400)


@require_http_methods(["GET", "POST"])
def login_request(request: HttpRequest) -> HttpResponse:
    """Render the login page and authenticates the user"""
    if request.htmx:
        template = "registration/partials/login.html"
    else:
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
    return HttpResponse(status_code=400)
