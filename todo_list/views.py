from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

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
    queryset = Task.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = "todo_list:task-list"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = "todo_list:task-list"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = "todo_list:task-list"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "todo_list/tags_list.html"
    queryset = Tag.objects.all().prefetch_related("tasks")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = "todo_list:tag-list"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = "todo_list:tag-list"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = "todo_list:tag-list"







