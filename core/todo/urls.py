from django.urls import path, include
from . import views


app_name = "todo"
urlpatterns = [
    path("", views.ToDoView.as_view(), name="index"),
    path("todo/<int:pk>/update/", views.ToDoUpdateview.as_view(), name="todo-update"),
    path("todo/<int:pk>/delete/", views.ToDoDeleteView.as_view(), name="todo-delete"),
    path("api/v1/", include("todo.api.v1.urls")),
]
