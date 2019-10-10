# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

admin.autodiscover()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # Redirect your homepage
        path('', RedirectView.as_view(url='task/')),

        # app tasks global links
        path('task/', include('tasks.urls'), name='tasks'),

        # admin link
        path('admin/', admin.site.urls),
    ]
