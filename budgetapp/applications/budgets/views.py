"""
model.py
"""
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET
from django.http.request import HttpRequest
from django.http.response import HttpResponse


@require_GET
def home_page(request: HttpRequest) -> HttpResponse:
    """
    Budgets home page
    """
    template = "budgets/home.html"
    return TemplateResponse(request, template)
