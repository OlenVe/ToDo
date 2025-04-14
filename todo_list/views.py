from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TagForm, TaskForm
from todo_list.models import Task, Tag


# def index(request):
#     task = Task.objects.all()
#     tags = Tag.objects.all()
#
#     context = {
#         "task": task,
#         "tags": tags,
#     }
#
#     return render(request, "todo_list/task_list.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo_list/task_list.html"
    queryset = Task.objects.all().prefetch_related("tags")



class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo_list:task-list")
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:task-list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "todo_list/tags_list.html"
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
    form_class = TagForm


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")


def change_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect(reverse_lazy("todo_list:task-list"))




