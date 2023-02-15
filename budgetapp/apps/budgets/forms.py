"""
forms.py
"""
from django import forms

from budgetapp.applications.budgets.models import Budget


class BudgetForm(forms.ModelForm):
    """Budget object form"""

    class Meta:
        model = Budget
        fields = ["name"]
