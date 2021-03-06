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

sys.path.append('/home/ubuntu/hunt')
sys.path.append('/home/hunt/hunt')
print >> sys.stderr, sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'hunt.settings'

# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()