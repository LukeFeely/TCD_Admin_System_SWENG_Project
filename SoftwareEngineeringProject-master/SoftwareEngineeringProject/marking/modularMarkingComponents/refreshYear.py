import os
import datetime
from distutils.dir_util import copy_tree
import subprocess

def refreshAllCurrent():
    for directory in os.listdir("./"):
        if(os.path.isdir(directory)):
           
            now = datetime.datetime.now()
            currentYear = str(now.year)
            os.chdir("./"+directory+"/"+currentYear)
            filename = "./updateDB.py"
            os.system("python "+filename)
            os.chdir("../../")
            print("\n")

def refreshAllForYear(year):
    for directory in os.listdir("./"):
        if(os.path.isdir(directory)):
           
            now = year
            currentYear = str(now.year)
            os.chdir("./"+directory+"/"+currentYear)
            filename = "./updateDB.py"
            os.system("python "+filename)
            os.chdir("../../")
            print("\n")

def refreshSpecificCourseCurrent(courseName):
    directoryFound = False
    for directory in os.listdir("./"):
        if(os.path.isdir(directory)):
            if(courseName == directory):
                directoryFound = True
                now = datetime.datetime.now()
                currentYear = str(now.year)
                os.chdir("./"+directory+"/"+currentYear)
                filename = "./updateDB.py"
                os.system("python "+filename)
                os.chdir("../../")
                print("\n")
    if(directoryFound == False):
        print("We could not find the course you are trying to update. The courses we have on record are:\n ")
        for directory in os.listdir("./"):
            if(os.path.isdir(directory)):
                print(directory)
        print("\nThere is no directory matching '" + courseName+"'" )



def refreshAllForCourseCurrent(courseName):
    directoryFound = False
    for directory in os.listdir("./"):
        if(os.path.isdir(directory)):
            if(courseName == directory):
                directoryFound = True
                now = datetime.datetime.now()
                for year in os.listdir("./"+directory):
                    if(year.isdigit()):
                        os.chdir("./"+courseName+"/"+year)
                        filename = "./updateDB.py"
                        os.system("python "+filename)
                        os.chdir("../../")
                    # print("\n")
    if(directoryFound == False):
        print("We could not find the course you are trying to update. The courses we have on record are:\n ")
        for directory in os.listdir("./"):
            if(os.path.isdir(directory)):
                print(directory)
        print("\nThere is no directory matching '" + courseName+"'" )

def refreshSpecificCourseForYear(courseName,year):
    directoryFound = False
    for directory in os.listdir("./"):
        if(os.path.isdir(directory)):
            if(courseName == directory):
                directoryFound = True
                now = year
                currentYear = year
                os.chdir("./"+directory+"/"+currentYear)
                filename = "./updateDB.py"
                os.system("python "+filename)
                os.chdir("../../")
                print("\n")
    if(directoryFound == False):
        print("We could not find the course you are trying to update. The courses we have on record are:\n ")
        for directory in os.listdir("./"):
            if(os.path.isdir(directory)):
                print(directory)
        print("\nThere is no directory matching '" + courseName+"'" )
            

def startNewYearAuto():
    courses = ["computerScience", "computerScienceAndBusiness"]
    yearToBaseOff = findMostRecentYear()
    yearToGenerate = datetime.datetime.now().year +1
    for directory in os.listdir("./"):
        if(os.path.isdir(directory)):
            if(directory in courses):
                copy_tree("./"+directory+"/"+str(yearToBaseOff), "./"+directory+"/"+str(yearToGenerate))
                os.chdir("./"+directory+"/"+str(yearToGenerate))
                os.system("python "+"./initialiseConfig.py "+str(yearToGenerate))
                os.chdir("../../")

def startNewYearSpecificYear(year):
    courses = ["computerScience", "computerScienceAndBusiness"]
    yearToBaseOff = findMostRecentYear()
    yearToGenerate = year
    for directory in os.listdir("./"):
        if(os.path.isdir(directory)):
            if(directory in courses):
                copy_tree("./"+directory+"/"+str(yearToBaseOff), "./"+directory+"/"+str(yearToGenerate))
                os.chdir("./"+directory+"/"+str(yearToGenerate))
                os.system("python "+"./initialiseConfig.py "+str(yearToGenerate))
                os.chdir("../../")

def findMostRecentYear():
    currentYear  = datetime.datetime.now().year
    checkYear = currentYear
    while(os.path.isdir("./computerScience/"+str(checkYear))==False):
        checkYear = checkYear -1
    return checkYear
    



#--------------------- Management Console -----------------------
#--------------------- Helper functions to validate IO ----------------
def acceptValidInput(question, listOfInputs):
    answer = input(question)
    while answer not in listOfInputs:
        print("Invalid Input!")
        answer = input(question)
    return answer

def acceptValidAnswer(answer, question ,listOfInputs, errMessage):
    
    while answer not in listOfInputs:
        print(errMessage)
        answer = input(question)
    return answer

def checkSecondArg(answer):
    while(((answer.isdigit() and int(answer) > 2000) or answer=='all') == False):
       answer = input("Error on second option.\nPlease input a year , 'all' or 'exit'\n>")
    return answer

def checkIntegerInput():
    answer = input("Select a year to generate or hit enter to default to the current year\n>")
    while ((answer not in ["exit" , ""]) and (((answer.isdigit() and int(answer) > 2000)) == False)):
        print("invalid input")
        answer = input("Select a year to generate or hit enter to default to the current year\n>")
    return answer

#--------------------- Helper functions to validate IO ----------------

print("Hello! Welcome to the managment console!")
courses = ["computerScience", "computerScienceAndBusiness"]
programme = acceptValidInput("what programme do you want to run?\n\noptions: [ refreshYear , newYear , exit ]\n >",["refreshYear","newYear","exit"])
if(programme == "refreshYear"):
    print("running refresh year programme")
    options1 = input("which course/year would you like to refresh?\n\noptions: [ [course:year] , [course] , [course:all] , [all:year] , [all]]\n>")
    selection = options1.split(":")
    el1 = None
    if(len(selection) > 1):
        validInputs = list(courses)
        validInputs.append("all")
        validInputs.append("exit")
        el1 = acceptValidAnswer(selection[0],"Please choose a course name, type all or exit\n>",validInputs,"first option error.")
        if(el1=="exit"):
            exit(0)
        el2 = checkSecondArg(selection[1])
        selection[0] = el1
        selection[1] = el2
    else:
        validInputs = list(courses)
        validInputs.append("all")
        validInputs.append("exit")
        el1 = acceptValidAnswer(selection[0],"Please choose a course name, type all or exit",validInputs,"first option error.")
        if(el1=="exit"):
            exit(0)
        selection[0] = el1

    if(selection[0]=="all"):
        print("Running a refresh on everything")
    if(selection[0] in courses):
        if(len(selection)==1):
            #refresh the course for the current year
            refreshSpecificCourseCurrent(selection[0])
        else:
            if(selection[1] == "all"):
                #refresh every year of a particular course
                print("refreshing "+selection[0] +" for every year on record")
                refreshAllForCourseCurrent(selection[0])
            elif(selection[1].isdigit() and int(selection[1]) > 2000):
                #refresh particular course for a particular year
                print("refreshing "+selection[0] +" for the year " + selection[1])
                refreshSpecificCourseForYear(selection[0],selection[1])
    elif(selection[0]=="all"):
        if(len(selection)==1):
            # refresh all courses for the current year
            refreshAllCurrent()
        elif(selection[1].isdigit() and int(selection[1]) > 2000):
                # refresh all the courses for a given year
                print("refreshing "+"all courses"+" for the year " + selection[1])
                refreshAllForYear(year)
    elif(selection[0]=="exit"):
        exit(0)
elif(programme == "newYear"):
    year = checkIntegerInput()
    if(year == ""):
        #makes a directory for current year + 1 in every course based on the most recent directory e.g 2020 will be based on 2019
        startNewYearAuto()
    if(year.isdigit() and int(year) > 2000):
        #makes a directory  for any given year in every course based on the most recent directory e.g 2023 will be based on 2019 if that is the most recent
        startNewYearSpecificYear(year)
       

#refreshSpecificCourseCurrent("computerScienceAndBusiness")