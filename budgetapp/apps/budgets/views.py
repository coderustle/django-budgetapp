"""
model.py
"""
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET


def index_page(request: HttpRequest) -> HttpResponse:
    """
    Public page.
    """
    if request.htmx:
        template = "partials/index.html"
    else:
        template = "index.html"
    return TemplateResponse(request, template)


@login_required
@require_GET
def home_page(request: HttpRequest) -> HttpResponse:
    """
    Budgets home page
    """
    template = "budget/home.html"
    return TemplateResponse(request, template)
