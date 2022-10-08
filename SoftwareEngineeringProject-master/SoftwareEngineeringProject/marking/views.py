from django.shortcuts import render
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import date
from marking.models import *
from marking.models import ICSProjectModel
from marking.models import ICSProjectModelDraft
from .forms import ICSProjectForm
from .forms import ICSProjectFormDraft
from django.core.mail import send_mail
from django.conf import settings
import re
from django.utils.encoding import smart_str
from django.views.static import serve
import os
import zipfile



from wsgiref.util import FileWrapper
from django.http import HttpResponse

'''
This method starts by calculating the total number of projects that the signed in user has that are corrected, not corrected, and have
conflicting marks. It then displays our dashboard.html file and passes in these variables to show a count to the user of all of these.
If the signed in user is a superuser, it counts the total number of projects that are corrected, uncorrected and have conflicting marks 
in the entire database.
'''
@login_required
def dashboard(request):
    all_projects_list = Project.objects.all()
    corrected_marks_count = 0
    conflicting_marks_count = 0
    not_corrected_marks_count = 0

    print(request.user.username)
    for project in all_projects_list:
        if(project.title =='Digest Algorithm for Efficient Message for Data Security'):
            print(project.readerOne  )
            print(project.title)
        if (project.readerOneHasMarked and project.readerOne == request.user.username) or (project.readerTWoHasMarked and project.readerTWo ==
                request.user.username) or ((project.readerOneHasMarked or project.readerTWoHasMarked) and request.user.is_superuser):
            corrected_marks_count = corrected_marks_count + 1
        if (project.supervisor == request.user.username or request.user.is_superuser) and project.readerOneHasMarked and project.readerTWoHasMarked and abs(
                project.readerOneMark - project.readerTWoMark) > project.allowedDifferenceInMarks:
            conflicting_marks_count = conflicting_marks_count + 1
        if (((project.readerOne == request.user.username or request.user.is_superuser) and project.readerOneHasMarked == False) or 
                ((project.readerTWo == request.user.username or request.user.is_superuser) and project.readerTWoHasMarked == False)):
            not_corrected_marks_count = not_corrected_marks_count + 1

    context = {'conflicting_marks_count': str(conflicting_marks_count),
               'corrected_marks_count': str(corrected_marks_count),
               'not_corrected_marks_count': str(not_corrected_marks_count)}

    return render(request, 'marking/dashboard.html', context)


'''
This methods takes in the projectid as a parameter. It gets this from the url that called it e.g. /marking/uncorrected/project/10/ will set
projectid = 10. This will pass the modular marking components and the project details of that projectid into marking_sheet.html which
displays the form for the logged in user to fill out. When submit is pressed the form is then passed to the submit method.
'''
@login_required
def marking_sheet(request, projectid):
    all_projects_list = Project.objects.all()
    project_list = []
    
    for project in all_projects_list:
        if str(project.projectid) == projectid and ((project.readerOne == request.user.username) 
            or (project.readerTWo == request.user.username) or request.user.is_superuser) : #ensure that logged in user is allowed to correct that project
                project_list.append(project)

    studentDetails = Student.objects.all()
    student = {}
    for details in studentDetails:
        if details.studentnumber == project_list[0].student:
            student = details

   
   
    # if(student):
    #     markingComponents = Content.objects.all().order_by('-orderOnPage').reverse()
    #     for component in markingComponents:
    #         if component.degreeId == student.degree:
    #             componentToAppend = component
    #             #print(component.inputBox)
    #             if("{{" in componentToAppend.inputBox):
    #                 text = re.search('{{(.*)}}',componentToAppend.inputBox).group(1)
    #                 print(text)
    #             markingComponentsList.append(componentToAppend) 

    #look for saved draft
    drafts = []
    data = None

    allDrafts = ICSProjectModelDraft.objects.all()
    for draft in allDrafts:
        if(draft.title == project_list[0].title):
            drafts.append(draft)

    if len(drafts) != 0:
        data = drafts[0]

    markingComponentsList = []
    
    componentsList = fetchCourseByYear(project_list[0].course, 2019)
    for content in componentsList:

        replaceData = ""
        start = content.inputBox.find("{{") 
        end = content.inputBox.find(" }}")
        if data != None:
            replaceData = (getattr(data,content.inputBox[(start+ 8):end]))
        content.inputBox = content.inputBox[0:start] + replaceData + content.inputBox[end+3: len(content.inputBox) - 1]
        markingComponentsList.append(content)

    if data == None:
        context = {'title': project_list[0].title,
                'courseName':markingComponentsList[0].degreeName,
                'student_number': project_list[0].student,
                'supervisor': project_list[0].supervisor,
                'date': date.today(),
                'components': markingComponentsList,
                }
    else:
        context = {'title': project_list[0].title,
                'courseName':markingComponentsList[0].degreeName,
                'student_number': project_list[0].student,
                'supervisor': project_list[0].supervisor,
                'date': date.today(),
                'components': markingComponentsList,
                'data' : data
                }
    return render(request, 'marking/marking_sheet.html', context)

'''
Lists all projects that the logged in user has corrected and allows them to click the view button to see what they've submitted. Allows
superusers to view all corrected marks pages.
'''
@login_required
def corrected_marks(request):
    all_projects_list = Project.objects.all()
    project_list = []

    for project in all_projects_list:
        if (project.readerOneHasMarked and project.readerOne == request.user.username) or (project.readerTWoHasMarked and project.readerTWo ==
                request.user.username) or ((project.readerOneHasMarked or project.readerTWoHasMarked) and request.user.is_superuser):
            project_list.append(project)

    context = {'project_list': project_list}

    return render(request, 'marking/corrected_marks.html', context)




'''
Lists all projects that the logged in user is a reader of with conflicting marks and allows them to see the difference in marks given.
Allows superusers to see all projects with mark differences
'''
@login_required
def conflicting_marks(request):
    all_projects_list = Project.objects.all()
    project_list = []

    for project in all_projects_list:
        if (project.supervisor == request.user.username or request.user.is_superuser) and project.readerOneHasMarked and project.readerTWoHasMarked \
                and abs(project.readerOneMark - project.readerTWoMark) > project.allowedDifferenceInMarks:
            project_list.append(project)

    context = {'project_list': project_list}

    return render(request, 'marking/conflicting_marks.html', context)

'''
Checks which projects the signed in user is assigned to that they haven't yet corrected. Passes this list to uncorrected.html to show
a list of projects with a mark button for each to allow marking. Page shows superusers all projects left to be marked.
'''
@login_required
def uncorrected_marks(request):
    all_projects_list = Project.objects.all()
    project_list = []

    for project in all_projects_list:
        if (((project.readerOne == request.user.username or request.user.is_superuser) and project.readerOneHasMarked == False) or 
                ((project.readerTWo == request.user.username or request.user.is_superuser) and project.readerTWoHasMarked == False)):
            project_list.append(project)

    context = {'project_list': project_list}

    return render(request, 'marking/uncorrected.html', context)

'''
A list of presentation times that the logged in user has upcoming and a list of previous presentation times are calculated for the logged in
user and passed to presentation_times.html to be displayed in a list.
'''
@login_required
def presentation_times(request):
    all_projects_list = Project.objects.all()
    upcoming_presentations = []
    past_presentations = []
    for project in all_projects_list:
        if (project.supervisor == request.user.username or request.user.is_superuser) and project.demodate >= date.today():
            upcoming_presentations.append(project)
        elif (project.supervisor == request.user.username or request.user.is_superuser) and project.demodate < date.today():
            past_presentations.append(project)

    context = {'upcoming_presentations': upcoming_presentations,
               'past_presentations' : past_presentations}
    return render(request, 'marking/presentation_times.html', context)

'''
Method is called when the submit button is pressed on a form. Form is validated to make sure all areas have been filled. If valid, boolean
that that reader has marked is set to true. EmailReminder function is called to let second reader know they need to mark if they haven't 
already. The completed form is displayed in viewmark method to show user it has saved successfully.
'''
@login_required
def submit(request):
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        if 'draftPressed' in request.POST:
            return draft(request)
        form = ICSProjectForm(request.POST)
    # check whether it's valid:
        if form.is_valid():
            test = form.save() #save as model to database.
            data = form.cleaned_data
            project = Project.objects.get(title = form.cleaned_data['title'])
            reader = 1 
            if(project.readerOne == request.user.username):
                project.readerOneHasMarked = True
                project.save()
            elif(project.readerTWo == request.user.username):
                project.readerTWoHasMarked = True
                project.save()
                reader = 2
            #calculate marks based on weightings
            calculateMark = (((form.cleaned_data['problems_motivation_analysis_weighting']/100) * (form.cleaned_data['problems_motivation_analysis_mark'])) +  ((form.cleaned_data['research_literature_review_analysis_weighting']/100) * (form.cleaned_data['research_literature_review_analysis_mark']))
                + ((form.cleaned_data['technical_content_project_execution_weighting']/100) * (form.cleaned_data['technical_content_project_execution_mark'])) + ((form.cleaned_data['testing_evaluation_analysis_conclusions_weighting']/100) * (form.cleaned_data['testing_evaluation_analysis_conclusions_mark']))
                + ((form.cleaned_data['presentation_and_writing_weighting']/100) * (form.cleaned_data['presentation_and_writing_mark'])))
            if reader == 1:
                project.readerOneMark = calculateMark
            elif reader == 2:
                project.readerTWoMark = calculateMark
            project.save()
            emailReminder(project)
            return render(request, 'marking/viewmarking.html', {'data': data})
    print(form.errors)
    return HttpResponseRedirect('../marking/invalid') #redirect to dashboard


@login_required
def draft(request):
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = ICSProjectFormDraft(request.POST)
        print("Trying to save a draft")
    # check whether it's valid:
        if form.is_valid():
            print("Valid Form Anyways")
            #delete any old drafts made for this project
            allDrafts = ICSProjectModelDraft.objects.all()
            for draft in allDrafts:
                if(draft.title == form.cleaned_data['title']): #we have matched the projectid with a stored form, display the form
                    deleteDraft = draft
                    deleteDraft.delete()
            test = form.save() #save as model to database.
            data = form.cleaned_data
            return render(request, 'marking/viewmarking.html', {'data': data})
    print(form.errors)
    return HttpResponseRedirect('../marking/invalid') #redirect to dashboard







'''
Method is called when the submit button is pressed and django determines that the form is invalid (not all components are filled out as
specified in the forms model). This dislays the simple invalid.html file letting the user know that they haven't filled out the form
as required.
'''
@login_required
def invalid(request):
    return render(request, 'marking/invalid.html')

'''
Viewmark page is called when the view button is pressed on a project in the corrected marks page. It will redirect to /viewmark/projectid.
This method will find the project of that projectid that thelogged in user is assigned to and display that project.
'''
@login_required
def viewmark(request, projectid):
    ProjectTitle = None
    all_projects_list = Project.objects.all()
    for project in all_projects_list:
        if str(project.projectid) == projectid:
            ProjectTitle = project.title #Get the title of the project with id projectid
            break

    allForms = ICSProjectModel.objects.all()
    for form in allForms:
        if(form.title == ProjectTitle): #we have matched the projectid with a stored form, display the form
            return render(request, 'marking/viewmarking.html', {'data': form})
    return render(request, 'marking/invalid.html')

'''
Called when a user successfully submits a mark for one of their projects. It sees if the other reader of the project has marked and emails
them a reminder to mark if they haven't already. 
'''
def emailReminder(project):
    if(project.readerOneHasMarked == True and project.readerTWoHasMarked == True):
        return
    else:
        if(project.readerOneHasMarked == True and project.readerTWoHasMarked == False):
            recipient_list = [project.readerTWoEmail,]
        else:
            recipient_list = [project.readerOneEmail,]
    subject = 'Reminder to mark project ' + project.title
    message = 'This is an email to notify you that reader one of project ' + str(project.id) + ' has completed marking. Your mark for this project is still needed. Thank you.'
    email_from = settings.EMAIL_HOST_USER
    send_mail( subject, message, email_from, recipient_list )
    return




from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt # (Allows file download with POST requests, can be omitted)
def zipFiles(request):
    print("processing file zip")
    set = PDF.objects.all()
  
    dir_path = os.path.dirname(os.path.realpath(__file__))
    ZipFile = zipfile.ZipFile("ziptest.zip", "w" )
    for file in set:
        fileName = settings.BASE_DIR+"/resultPDFs/"+file.file.name
        print(fileName)
        fileZip = open(fileName,"r")
        ZipFile.write("resultPDFs/"+file.file.name, compress_type=zipfile.ZIP_DEFLATED)
    ZipFile.close()
   
   
    filename = set[0].file.name.split('/')[-1]
    response = HttpResponse(open("./ziptest.zip", 'rb'), content_type='application/zip')
    response['Content-Disposition'] = 'attachment;filename="%s"' % 'download.zip'

    return response
   





def acceptMarkingPDF(request,projectid):
    #request is like a dictionary which we can query using .get()
    #.get the file that the client submitted 
    file = request.FILES.get('pdfFile')
    #write that file to the database
    pdfFile = PDF()
    pdfFile.title = file.name
    pdfFile.file = file
    pdfFile.save()
    #write http response back to the clientside javascript in correctedMarks.html
    data = [{
    "result": "success"
    
  }]
    response = HttpResponse(data,content_type='application/json')
    
    response.status_code = 200

    return HttpResponse(response)


def checkFormValidity(request):
    form = ICSProjectForm(request.POST)
    
    if(form.is_valid()):
        response = HttpResponse("success",content_type='text')
        response.status_code = 200
        return HttpResponse(response)
    else:
        response = HttpResponse("error",content_type='text')
        response.status_code = 406
        return HttpResponse(response)


