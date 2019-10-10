# -*- coding: utf-8 -*-

from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from weasyprint import HTML

from tasks.models import Task
from tasks.forms import TaskForm

TASK_LIST_URL = reverse_lazy('tasks:tasks-list')

# Management for the Tasks
class TasksView(ListView):
    template_name = "tasks/tasks-list.html"
    model = Task

# delete the task finished
def clear_resolved_tasks(request):
    if request.method == 'POST':
        # Modify an object in POST only
        Task.objects.filter(is_resolved=True).delete()

    return HttpResponseRedirect(TASK_LIST_URL)


# all tasks finish view
def toggle_tasks(request):
    if request.method == 'POST':
        # Modify an object in post only
        try:
            task = Task.objects.all()[0]
        except IndexError:
            task = None

        if task is not None:
            status = not task.is_resolved
            Task.objects.all().update(is_resolved=status)

    return HttpResponseRedirect(TASK_LIST_URL)


# Gestion du formulaire forms.py
class TaskCreateView(CreateView):
    form_class = TaskForm
    success_url = TASK_LIST_URL

    def form_invalid(self, form):
        # erreurs du formulaire non affiché
        return HttpResponseRedirect(self.success_url)


# task finish view
def toggle_task(request, task_id):
    if request.method == 'POST':
        # Modify an object in post only
        task = get_object_or_404(Task, pk=task_id)

        task.is_resolved = not task.is_resolved
        task.save()

    return HttpResponseRedirect(TASK_LIST_URL)

# delete view
class TaskDeleteView(DeleteView):
    model = Task
    success_url = TASK_LIST_URL

# download view
def task_download(request):
    if 'download-file' in request.method == 'POST':
        task = request.get_object(file='download-file')

    html_template = render_to_string('tasks/tasks-list.html')
    pdf_file = HTML(string=html_template).write_pdf(target="/tmp/task-list.pdf");

    file_system = FileSystemStorage('/tmp')
    with file_system.open('task-list.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="task.pdf"'
        return response

    return response
