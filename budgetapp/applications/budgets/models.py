from django.db import models


class Budget(models.Model):
    name = models.CharField(null=False, max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ("-created",)
        indexes = [
            models.Index(fields=["-created"]),
        ]
