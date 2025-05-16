from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from list.models import Task, Tag


class HomeListView(ListView):
    model = Task
    template_name = "listed/index.html"
    context_object_name = "tasks"


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "listed/task_update.html"
    context_object_name = "task"
    fields = "__all__"
    success_url = "/"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "listed/task_confirmation_delete.html"
    context_object_name = "task"
    success_url = "/"


class TaskCreateView(CreateView):
    model = Task
    template_name = "listed/task_create.html"
    context_object_name = "task"
    fields = "__all__"
    success_url = "/"


class TagListView(ListView):
    model = Tag
    template_name = "listed/tag.html"
    context_object_name = "tags"


class TagUpdateView(UpdateView):
    model = Tag
    template_name = "listed/tag_update.html"
    context_object_name = "tag"
    fields = "__all__"
    success_url = "/tags/"


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "listed/tag_confirmation_delete.html"
    context_object_name = "tag"
    success_url = "/tags/"


class TagCreateView(CreateView):
    model = Tag
    template_name = "listed/tag_create.html"
    context_object_name = "tag"
    fields = "__all__"
    success_url = "/tags/"


def toggle_task_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return redirect("to-do-list:index")
