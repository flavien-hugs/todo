# -*- coding: utf-8 -*-

from django.urls import path, include
from tasks.views import *

app_name = 'tasks'
urlpatterns = [
    # url list
    path('', TasksView.as_view(), name='tasks-list'),
    # url delete
    path('delete/', clear_resolved_tasks, name="tasks-clear"),
    # all url finish
    path('toggle/', toggle_tasks, name="tasks-toggle"),

    # url add
    path('add/', TaskCreateView.as_view(), name='task-create'),
    # url finish
    path('toggle/<task_id>/', toggle_task, name="task-toggle"),
    # delete url finish
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name="task-delete"),

    # download url
    path('download/', task_download, name="task-download"),
]
