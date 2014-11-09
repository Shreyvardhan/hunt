"""
WSGI config for hunt project.

It exposes the WSGI callable as a module-level variable named ``application``.
Doe
For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir('/home/ubuntu/.virtualenvs/hunt/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'hunt.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()