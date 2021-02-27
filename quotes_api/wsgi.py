"""
WSGI config for quotes_api project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

from dj_static import Cling

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes_api.settings')

application = Cling(get_wsgi_application())
