from django.db import models


class NumberQueryLogs(models.Model):
    queried_number = models.IntegerField(null=False, blank=False, unique=True)
    count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_queried_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.queried_number} -> {self.count}"

