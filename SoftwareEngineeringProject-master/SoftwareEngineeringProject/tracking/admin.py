

from django.contrib import admin

# Register your models here.

from .models import Student, Supervisor, Project, Degree

admin.site.register(Student)
admin.site.register(Supervisor)
admin.site.register(Project)
admin.site.register(Degree)
