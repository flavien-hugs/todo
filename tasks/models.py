# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

# my models here.
class Task(models.Model):
    content = models.CharField(_(u'task'), max_length=225, null=True, blank=True)
    is_resolved = models.BooleanField(_(u'Resolved ?'), null=True, blank=True)

    def __str__(self):
        return u'Task %d : %s' % (self.id, self.content)
