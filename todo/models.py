from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusType(models.IntegerChoices):
    todo = 1, _("To Do")
    doing = 2, _("Doing")
    done = 3, _("Done")


class ToDo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(
        choices=StatusType.choices, default=StatusType.todo.value)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
