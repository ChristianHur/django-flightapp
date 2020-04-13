"""
WSGI config for flightscheduler project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flightscheduler.settings')

application = get_wsgi_application()
#application = DjangoWhiteNoise(application)

# Configure Django App for Heroku.
# import django_heroku
# django_heroku.settings(locals())