from django.urls import path, include

from list.views import (
    HomeListView,
    TagListView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCreateView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView,
    toggle_task_done,
)

app_name = "to-do-list"

urlpatterns = [
    path("", HomeListView.as_view(), name="index"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("task/<int:pk>/toggle/", toggle_task_done, name="task-toggle"),
]
