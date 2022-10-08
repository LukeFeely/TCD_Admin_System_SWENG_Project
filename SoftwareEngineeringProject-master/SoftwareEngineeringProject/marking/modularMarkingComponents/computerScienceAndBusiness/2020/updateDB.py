import sys
import os.path
absolutePath = (os.path.realpath(__file__))
rootIndex = absolutePath.rfind('SoftwareEngineeringProject') + len("SoftwareEngineeringProject")
relativePath = absolutePath[:rootIndex] +"/"
sys.path.append(relativePath)
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SoftwareEngineeringProject.settings")
import django
from django.conf import settings
import sys
path = settings.BASE_DIR
sys.path.append(path)
import django
django.setup()
from marking.models import *
import codecs
from config import markingScheme


filesFound = True
fileNotFound = ""
for key in markingScheme:
        
        if(key!= "courseName" and key != "courseNumber" and key != "year"):
            filesFound = os.path.isfile("./" + markingScheme[str(key)]['outline']+".html")
            if(filesFound==False):
                fileNotFound = markingScheme[str(key)]['outline']+".html"
                break

if(filesFound):

    def htmlToString(filename):
        filepath = "./"+filename+".html"
        f=codecs.open(filepath, 'r')
        html = str(f.read())
        indexOfBody = html.index("<body>")+6
        endOfBody = html.index("</body>")
        return html[indexOfBody:endOfBody]
    i = 1
    length = len(markingScheme.keys())-3
    resetFormOrder(markingScheme["courseNumber"],markingScheme["year"])
    print("collecting entries for: "+ markingScheme['courseName'])
    print("writing...")
    for key in markingScheme:
        
        if(key!= "courseName" and key != "courseNumber" and key != "year"):

            newContent = Content()
            newContent.contentId = 8
            newContent.description =  htmlToString(markingScheme[str(key)]['outline'])
            newContent.inputBox = htmlToString(markingScheme[str(key)]['input'])
            newContent.defaultWeight = markingScheme[str(key)]['defaultWeight']
            newContent.weighted = True
            newContent.degreeId = markingScheme['courseNumber']
            newContent.degreeName = markingScheme['courseName']
            newContent.section = 2
            newContent.title = markingScheme[str(key)]['title']
            newContent.orderOnPage = i
            newContent.year = markingScheme["year"]
            safeInsertContentToDB(newContent)
            
            print(str((i*100)/length) + "%"+"...")
            i = i+1
            


    print("saved all the entries to the database!")
else:
    print("-----------------------------")
    print("Script Error: Missing File\n\n")
    print("Cant seem to find your files??")
    print("Please check the name of "+ fileNotFound+" in "+markingScheme['courseName']+ " for the year "+ str(markingScheme["year"]))
    print("\n\n")







