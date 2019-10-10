# -*- coding: utf-8 -*-

from django import forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # genere resolved a un autre endroit
        exclude = ('is_resolved',)
