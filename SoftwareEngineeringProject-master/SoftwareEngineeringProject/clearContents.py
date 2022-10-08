#exec(open('update.py').read())
import os
from django.core.wsgi import get_wsgi_application
from django.db import models
os.environ['DJANGO_SETTINGS_MODULE'] = 'SoftwareEngineeringProject.settings'
application = get_wsgi_application()

#most load models after the application is initialized
from marking.models import *
import codecs



set  = Content.objects.all()
for obj in set:
    obj.delete()