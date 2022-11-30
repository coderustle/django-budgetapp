from django.contrib import admin

from budgetapp.applications.budgets.models import Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    pass
