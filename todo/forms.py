from django import forms
from .models import ToDo


class ToDoFormClass(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = "form-control"
