from django.urls import path
from django.conf.urls import include
from .views import ProjectCreateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adminstudents/', views.StudentsListView.as_view(), name='Students'),
    path('adminsupervisors/', views.Supervisors, name='Supervisors'),
    path('new/',ProjectCreateView.as_view(),name='Create')
]