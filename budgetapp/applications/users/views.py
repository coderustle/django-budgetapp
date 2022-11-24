"""
Django views
"""
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from .forms import NewUserForm


@require_http_methods(["GET", "POST"])
def register_page(request: HttpRequest) -> HttpResponse:
    """Render register page and create new user"""
    template = "registration/register.html"

    if request.method == "GET":
        form = NewUserForm()
        context = {"form": form}
        return TemplateResponse(request, template=template, context=context)
