from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class StatusType(models.IntegerChoices):
    todo = 1, _("To Do")
    doing = 2, _("Doing")
    done = 3, _("Done")
    
class PriorityType(models.IntegerChoices):
    low = 1, _("Low")
    medium = 2, _("Medium")
    high = 3, _("High")


class ToDo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=StatusType.choices, default=StatusType.todo.value)
    priority = models.IntegerField(choices=PriorityType.choices, default=PriorityType.low.value)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
