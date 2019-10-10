# -*- coding: utf-8 -*-
"""
tasks: test
"""

from django.test import TestCase
from django.urls import reverse

from tasks.models import Task

# Test sur les views
class TaskTest(TestCase):

    # liste de tâche reprenant tous les cas de figures
    def setUp(self):
        task_1 = Task.objects.create(content=u'first task', is_resolved=True)
        task_2 = Task.objects.create(content=u'second task', is_resolved=False)
        task_3 = Task.objects.create(content=u'third task', is_resolved=True)
        task_4 = Task.objects.create(content=u'four task', is_resolved=False)

    # ajout des méthodes, une méthode par test
    def test_task_list(self):
        url = reverse('tasks-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), Task.objects.count())

    # Test de la suppression des taches terminées
    def test_tasks_clear(self):
        url = reverse('tasks-clear')

        nb_tasks = Task.objects.count()
        response = self.client.post(url)
        self.assertEqual(nb_tasks-2, Task.objects.count())

    # Test de changement de status de toutes les tâches
    def test_tasks_toggle(self):
        url = reverse('tasks-toggle')

        nb_tasks = Task.objects.filter(is_resolved=True).count()
        response = self.client.post(url)
        self.assertEqual(0, Task.objects.filter(is_resolved=True).count())

        response = self.client.post(url)
        self.assertEqual(nb_tasks+2, Task.objects.filter(is_resolved=True).count())

    # Test de création d’une tâche
    def test_tasks_create(self):
        url = reverse('tasks-create')

        nb_tasks = Task.objects.count()
        response = self.client.post(url, {'content': u'first task'})
        self.assertEqual(nb_tasks+1, Task.objects.count())

    # Test de changement de statut d’une tâche
    def test_task_toggle(self):
        task_id = Task.objects.all()[0].id
        url = reverse('task-toggle', args={task_id})

        status = Task.objects.get(pk=task_id).is_resolved
        response = self.client.post(url)
        self.assertEqual(status, not Task.objects.get(pk=task_id).is_resolved)

    # Test de la suppression d’une tâche
    def test_task_delete(self):
        task_id = Task.objects.all()[0].id
        url = reverse('task-toggle', args={task_id})

        nb_tasks = Task.objects.count()
        response = self.client.post(url)
        self.assertEqual(nb_tasks-1, Task.objects.count())

        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)

