from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Project(models.Model):
    class Meta:
        indexes = [
             models.Index(fields=['supervisor']),
        ]
    title = models.CharField(max_length=250, null=True, blank = True)
    supervisor = models.ForeignKey('Supervisor', on_delete = models.PROTECT, null=True, related_name='supervisor')
    student = models.ForeignKey('Student',on_delete = models.CASCADE, null = True)
    secondReader = models.ForeignKey('Supervisor', null=True, blank=True, on_delete = models.SET_NULL, related_name='secondReader')
    demoDate = models.DateField(null=True, blank = True)
    demoTime = models.TimeField(null=True, blank = True)
    demoOrganiser = models.ForeignKey('Supervisor', null=True, blank = True, on_delete = models.SET_NULL, related_name='demoOrganiser')
    demoLocation = models.CharField(max_length=50, null=True, blank = True)
    #projectid = models.AutoField(default=0, primary_key = True)
    #supervisorHasMarked = models.BooleanField(default=False, null=False)
    #secondReaderHasMarked = models.BooleanField(default=False, null=False)
    #supervisorMark = models.PositiveIntegerField(default=0, null=False)
    #secondReaderMark = models.PositiveIntegerField(default=0, null=False)
    #differenceInMarks = models.PositiveIntegerField(default=0, null=False)
    #allowedDifferenceInMarks = models.PositiveIntegerField(default=10, null=False)
    #supervisorHasDraft = models.BooleanField(default=False, null=False)
    #secondReaderHasDraft = models.BooleanField(default=False, null=False)
    #course = models.PositiveIntegerField(default=33, null=False) # default course is ICS


    def __str__(self):
        return '%s' % (self.title)

    def get_absolute_url(self):
        return reverse('loginredirect')



class Student(models.Model):
    class Meta:
         indexes = [
             models.Index(fields=['surname']),
             models.Index(fields=['firstName']),
             models.Index(fields=['studentNumber']),
             models.Index(fields=['degree']),
             models.Index(fields=['year']),
         ]
    surname = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    email = models.EmailField(max_length=40, null=True, blank = True)
    studentNumber = models.PositiveIntegerField()
    degree = models.ForeignKey('Degree', on_delete = models.PROTECT, null=True)
    year = models.CharField(max_length=9, null=True, blank = True)
    doingCompSciProject = models.ForeignKey('Project', null=True, blank = True, on_delete = models.SET_NULL, related_name='+')

    def __str__(self):
        return '%s %s' % (self.firstName, self.surname)

class Supervisor(models.Model):
    class Meta:
        indexes=[
            models.Index(fields=['surname']),
            models.Index(fields=['firstname']),
            models.Index(fields=['initials'])
        ]

    surname=models.CharField(max_length=30)
    firstname=models.CharField(max_length=30)
    email=models.EmailField(null=True, blank = True, max_length=40)
    initials=models.CharField(max_length=30)
    max_students_to_supervise=models.PositiveSmallIntegerField(null=True, blank = True)
    max_students_to_second_read=models.PositiveSmallIntegerField(null=True, blank = True)
    grade=models.CharField(null=True, blank = True, max_length=20)
    year_of_appointment=models.PositiveSmallIntegerField(null=True, blank = True)
    username=models.CharField(null=True, blank = True, max_length=40)
    user_type=models.CharField(null=True, blank = True, max_length=40)
    status=models.CharField(null=True, blank = True, max_length=8)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s %s' % (self.firstname, self.surname)


class Degree(models.Model):
    degree_name=models.CharField(null=True, blank = True, max_length=50)

    def __str__(self):
        return '%s' % (self.degree_name)
