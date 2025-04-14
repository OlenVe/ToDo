from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from todo_list.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created", "deadline", "is_done")
    list_filter = ("is_done", "deadline")
    search_fields = ("content",)
    filter_horizontal = ("tags",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)



