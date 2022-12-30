"""
model.py
"""
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

from budgetapp.applications.users.models import User


@login_required
@require_GET
def home_page(request: HttpRequest) -> HttpResponse:
    """
    Budgets home page
    """
    template = "budget/home.html"
    return TemplateResponse(request, template)