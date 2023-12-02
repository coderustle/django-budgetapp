from django.db import models
from django.urls import reverse

from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase


class Budget(models.Model):
    name = models.CharField(null=False, max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)
        indexes = [
            models.Index(fields=["-created"]),
        ]
        default_permissions = ("add", "change", "delete")
        permissions = (("view_budget", "View Budget Objects"),)
        get_latest_by = "created"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("budget:details", kwargs={"pk": self.pk})


class BudgetUserObjectPermission(UserObjectPermissionBase):
    content_object = models.ForeignKey(Budget, on_delete=models.CASCADE)


class BudgetGroupObjectPermission(GroupObjectPermissionBase):
    content_object = models.ForeignKey(Budget, on_delete=models.CASCADE)
