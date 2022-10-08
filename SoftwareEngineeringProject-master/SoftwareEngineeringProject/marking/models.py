from django.db import models
import datetime

# Create your models here.

class Degree(models.Model):
	degreeid = models.PositiveIntegerField(null=False)
	degree_name = models.CharField(max_length=50, null=False)

class Content(models.Model):
	contentId = models.IntegerField(null = False)
	title = models.CharField(max_length = 200)
	description =  models.CharField(max_length = 10000)
	inputBox = models.CharField(max_length = 1000)
	defaultWeight = models.IntegerField(default=20)
	weighted = models.BooleanField(default=True)
	degreeId = models.IntegerField(null = False)
	degreeName = models.CharField(max_length = 200)
	section = models.IntegerField(null = False)
	year = models.IntegerField(null = False)
	orderOnPage = models.IntegerField(default=1)

	def toString(self):
		return (self.title)
	
	def print(self):
		print(self.toString())

	def resetOrderOnPage(self):
		self.orderOnPage = 0
		self.save()

	def updateTitle(self,newTitle):
		self.title = newTitle
		self.save()

	
	def copyAttributes(self,contentToCopy):
		self.contentId = contentToCopy.contentId 
		self.title = contentToCopy.title 
		self.description = contentToCopy.description 
		self.inputBox = contentToCopy.inputBox 
		self.defaultWeight = contentToCopy.defaultWeight 
		self.weighted = contentToCopy.weighted 
		self.degreeId = contentToCopy.degreeId 
		self.degreeName = contentToCopy.degreeName 
		self.section = contentToCopy.section 
		self.year = contentToCopy.year 
		self.orderOnPage = contentToCopy.orderOnPage 

#helper functions for implementing modularity
def filterByYear(year):
	results = Content.objects.filter(year = year )
	return results

def listContent():
	allContent = Content.objects.all()
	for content in allContent:
		content.print()

def resetFormOrder(degreeId,year):
	entriesForYear = filterByYear(year)
	for entry in entriesForYear:
		if(entry.degreeId == degreeId):
			entry.resetOrderOnPage()

def getByTitle(title):
	results = Content.objects.filter(title = title )
	if(len(results) >0):
		return results[0]
	else:
		return None

def getByHtml(htmlDescription):
	results = Content.objects.filter(description = htmlDescription)
	if(len(results) >0):
		return results[0]
	else:
		return None

def fetchCourseByYear(courseCode, year):
	# today = datetime.datetime.now()
	# currentYear = today.year
	return Content.objects.filter(degreeId = courseCode, year = year)

def fetchContentsForPage(courseCode,year):
	currentObjects = fetchCourseByYear(courseCode,year)
	displayableObjects = []
	for obj in currentObjects:
		if obj.orderOnPage > 0 :
			displayableObjects.append(obj)
	return displayableObjects

def printContentSet(contentSet):
	for content in contentSet:
		content.print()
	

def contentExists(title,courseCode,htmlDescription = ""):
	titleCheck = getByTitle(title)
	htmlCheck = getByHtml(htmlDescription)
	if(titleCheck != None and titleCheck.degreeId == courseCode):
		return True
	elif(htmlCheck!= None and htmlCheck.degreeId == courseCode ):
		return True
	else:
		return False

def getContentIfExists(title,courseCode,htmlDescription = ""):
	if(contentExists(title,courseCode,htmlDescription)):
		sameTitle = getByTitle(title)
		sameDescription = getByHtml(htmlDescription)
		if(sameTitle!= None):
			return sameTitle
		elif(sameDescription!=None):
			return sameDescription
	else:
		return None

def safeInsertContentToDB(newContent):
	sameContentExists = getContentIfExists(newContent.title,newContent.degreeId,newContent.description)
	if(sameContentExists != None and sameContentExists.year == newContent.year):
		sameContentExists.copyAttributes(newContent)
		sameContentExists.save()
	else:
		newContent.save()




class Student(models.Model):
	studentid = models.PositiveIntegerField(null=False)
	surname = models.CharField(max_length=30, null=False)
	firstname = models.CharField(max_length=30, null=False)
	email = models.CharField(max_length=40, null=False)
	studentnumber = models.IntegerField(null=False)
	degree = models.PositiveIntegerField(null=False)
	year = models.CharField(max_length=9, null=True)
	doing_compsci_project = models.PositiveIntegerField(null=True)


class Project(models.Model):
	projectid = models.PositiveIntegerField(null=False)
	title = models.CharField(max_length=250, null=False)
	supervisor = models.CharField(max_length=250, null=False)
	supervisorid = models.PositiveIntegerField(null=False)
	student = models.PositiveIntegerField(null=False)
	second_reader = models.PositiveIntegerField(null=True) 
	demodate = models.DateField(("Date"), blank=True)
	demotime = models.TimeField(("Time"), blank=True)
	demoorganiser = models.PositiveIntegerField(null=True)
	demolocation = models.CharField(max_length=50, null=True)
	readerOneHasMarked = models.BooleanField(default=False, null=False)
	readerTWoHasMarked = models.BooleanField(default=False, null=False)
	readerOneMark = models.PositiveIntegerField(default=0, null=False)
	readerTWoMark = models.PositiveIntegerField(default=0, null=False)
	differenceInMarks = models.PositiveIntegerField(default=0, null=False)
	allowedDifferenceInMarks = models.PositiveIntegerField(default=10, null=False)
	readerOneHasDraft = models.BooleanField(default=False, null=False)
	readerTWoHasDraft = models.BooleanField(default=False, null=False)
	readerOne = models.CharField(default='', max_length=250, null=False)
	readerTWo = models.CharField(default='', max_length=250, null=False)
	readerOneEmail = models.CharField(default='', max_length=250, null=False)
	readerTWoEmail = models.CharField(default='', max_length=250, null=False)
	course = models.PositiveIntegerField(default=33, null=False) # default course is ICS

	def print(self):
		print(self.title)
		print(self.supervisorid)
		print(self.supervisor)
		

def printAllProjects():
	set = Project.objects.all()
	for el in set:
		el.print()

class Supervisor(models.Model):
	supervisorid = models.PositiveIntegerField(null=False)
	surname = models.CharField(max_length=30, null=False)
	firstname = models.CharField(max_length=30, null=False)
	email = models.CharField(max_length=40, null=False)
	initials = models.CharField(max_length=30, null=False)
	max_students_to_supervise = models.PositiveIntegerField(null=True)
	max_students_to_second_read = models.PositiveIntegerField(null=True)
	grade = models.CharField(max_length=20, null=True)
	year_of_appointment = models.PositiveIntegerField(null=True)
	username = models.CharField(max_length=40, null=False)
	user_type = models.CharField(max_length=40, null=True)
	status = models.CharField(max_length=8, null=True)

class ICSProjectModel(models.Model):
	title = models.CharField(max_length = 500)
	studentid = models.CharField(max_length = 500)
	supervisor = models.CharField(max_length = 500)
	date = models.CharField(max_length = 500)
	scopes_and_aims = models.CharField(max_length = 500)
	challenges = models.CharField(max_length = 500)
	problems_motivation_analysis = models.CharField(max_length = 500)
	problems_motivation_analysis_weighting = models.IntegerField()
	problems_motivation_analysis_mark = models.IntegerField()
	research_literature_review = models.CharField(max_length = 500)
	research_literature_review_analysis_weighting = models.IntegerField()
	research_literature_review_analysis_mark = models.IntegerField()
	technical_content_project_execution = models.CharField(max_length = 500)
	technical_content_project_execution_weighting = models.IntegerField()
	technical_content_project_execution_mark = models.IntegerField()
	testing_evaluation_analysis_conclusions = models.CharField(max_length = 500)
	testing_evaluation_analysis_conclusions_weighting = models.IntegerField()
	testing_evaluation_analysis_conclusions_mark = models.IntegerField()
	presentation_and_writing = models.CharField(max_length = 500)
	presentation_and_writing_weighting = models.IntegerField()
	presentation_and_writing_mark = models.IntegerField()


class ICSProjectModelDraft(models.Model):
	title = models.CharField(max_length = 500, blank=True)
	studentid = models.CharField(max_length = 500, blank=True)
	supervisor = models.CharField(max_length = 500, blank=True)
	date = models.CharField(max_length = 500, blank=True)
	scopes_and_aims = models.CharField(max_length = 500, blank=True)
	challenges = models.CharField(max_length = 500, blank=True)
	problems_motivation_analysis = models.CharField(max_length = 500, blank=True)
	problems_motivation_analysis_weighting = models.IntegerField(blank=True, null=True)
	problems_motivation_analysis_mark = models.IntegerField(blank=True, null=True)
	research_literature_review = models.CharField(max_length = 500, blank=True)
	research_literature_review_analysis_weighting = models.IntegerField(blank=True, null=True)
	research_literature_review_analysis_mark = models.IntegerField(blank=True, null=True)
	technical_content_project_execution = models.CharField(max_length = 500, blank=True)
	technical_content_project_execution_weighting = models.IntegerField(blank=True, null=True)
	technical_content_project_execution_mark = models.IntegerField(blank=True, null=True)
	testing_evaluation_analysis_conclusions = models.CharField(max_length = 500, blank=True)
	testing_evaluation_analysis_conclusions_weighting = models.IntegerField(blank=True, null=True)
	testing_evaluation_analysis_conclusions_mark = models.IntegerField(blank=True, null=True)
	presentation_and_writing = models.CharField(max_length = 500, blank=True)
	presentation_and_writing_weighting = models.IntegerField(blank=True, null=True)
	presentation_and_writing_mark = models.IntegerField(blank=True, null=True)
	
class PDF(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
	
	
	
def clearAllPDF():
	set = PDF.objects.all()
	for file in set:
		file.delete()


def listPDFs():
	set = PDF.objects.all()
	for file in set:
		print(file.title)

#note django ignores max length of integers


