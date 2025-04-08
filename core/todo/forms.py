from django import forms
from .models import ToDo


class ToDoFormClass(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ("title", "description", "status", "priority")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["class"] = "form-control"
        self.fields["description"].widget.attrs["class"] = "form-control"
        self.fields["description"].widget.attrs["rows"] = "5"
        self.fields["status"].widget.attrs["class"] = "form-select"
        self.fields["priority"].widget.attrs["class"] = "form-select"
