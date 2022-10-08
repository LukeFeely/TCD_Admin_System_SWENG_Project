#exec(open('update.py').read())
import zipfile
import zlib
import os
from django.core.wsgi import get_wsgi_application
from django.db import models
os.environ['DJANGO_SETTINGS_MODULE'] = 'SoftwareEngineeringProject.settings'
application = get_wsgi_application()

#most load models after the application is initialized
from marking.models import *
import codecs



def htmlToString(filename):
    filepath = "./marking/modularMarkingComponents/"+filename
    f=codecs.open(filepath, 'r')
    html = str(f.read())
    indexOfBody = html.index("<body>")+6
    endOfBody = html.index("</body>")
    return html[indexOfBody:endOfBody]

#take user input to populate field in Django database
# filename1 = input("file path to marking outline html?")
# filename2 = input("file path to input box html?")
# courseCode = input("course number?")
# courseName = input("course name?")
# section = input("what section?")


# newContent = Content()
# newContent.contentId = 8
# newContent.description =  htmlToString(filename1)
# newContent.inputBox = htmlToString(filename2)
# newContent.defaultWeight = 20
# newContent.weighted = True
# newContent.degreeId = courseCode
# newContent.degreeName = courseName
# newContent.section = section
# newContent.year = 2019
# newContent.save()

with zipfile.ZipFile('test'+ '.zip', 'w') as myzip:
    f = open('test.html').read()
    myzip.write(f)
    myzip.write('pyShell.sh')