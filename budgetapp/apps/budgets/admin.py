from django.contrib import admin

from budgetapp.apps.budgets.models import Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    pass
