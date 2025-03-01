from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import ToDo
from .forms import ToDoFormClass


# Create your views here.
class ToDoView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "todo/index.html"
    form_class = ToDoFormClass
    success_url = reverse_lazy("todo:index")
    success_message = "Your Task has been add."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = ToDo.objects.all()
        return context
    
    

class ToDoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    queryset = ToDo.objects.all()
    http_method_names = ["post"]
    success_message = "The skill was Deleted successfully."
    success_url = reverse_lazy("todo:index")



class ToDoUpdateview(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "todo/todo-update.html"
    queryset = ToDo.objects.all()
    form_class = ToDoFormClass
    success_message = "The Task was Updated successfully."
    success_url = reverse_lazy("todo:index")
