from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Project, Supervisor, Degree
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

project_data = Project.objects.all()
supervisor_data = Supervisor.objects.all()


def index(request):
    html = "<html><body><h1>Tracking Page</h1><p>Hello World</p></body></html>"
    return HttpResponse(html)

class ProjectCreateView(LoginRequiredMixin, CreateView): #super().form_valid(form)
    model = Project
    fields=['title', 'student', 'supervisor'] #'supervisor'

    def form_valid(self, form):
        form.instance.author=self.request.user

        proj = form.save()
        student = proj.student
        student.doingCompSciProject = proj
        student.save()
        return super().form_valid(form) 

class StudentsListView(ListView):
    template_name = 'tracking/Students.html'

    def get_queryset(self):
        return Student.objects.all()

def Supervisors(request):
    proj_count = {}
    for supervisor in supervisor_data:
        proj_count[supervisor.surname] = len(Project.objects.filter(supervisor=supervisor))

    context = {
        'supervisors': supervisor_data,
        'projects': project_data,
        'proj_count' : proj_count
    }
    return render(request, 'tracking/Supervisors.html', context)

def home(request):
    return render(request, 'tracking/trackinghome.html')    