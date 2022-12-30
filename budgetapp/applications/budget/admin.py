from django.contrib import admin

from budgetapp.applications.budget.models import Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    pass
