from django.urls import path

from . import views

app_name = 'marking'

urlpatterns = [
    # /marking/
    path('', views.dashboard, name='dashboard'),

    # /marking/corrected/
    path('corrected/', views.corrected_marks, name='corrected_marks'),

    # /utility to zip files/
    path('corrected/zip', views.zipFiles, name='corrected_marks'),

    # marking/conflicting/
    path('conflicting/', views.conflicting_marks, name='conflicting_marks'),

    # marking/uncorrected/
    path('uncorrected/', views.uncorrected_marks, name='uncorrected_marks'),

    # /marking/uncorrected/project/projectid/
    path('uncorrected/project/<projectid>/', views.marking_sheet, name='marking_sheet'),


    path('uncorrected/project/<projectid>/blob/',views.acceptMarkingPDF,name = "PDFSubmit") ,

    # marking/presentations/
    path('presentations/', views.presentation_times, name='presentations'),

    # marking/submit/projectid
    path('submit', views.submit, name='submit'),

    path('draft', views.draft, name='draft'),

    # marking/invalid
    path('invalid', views.invalid, name='invalid'),

    # marking/viewmark/project/projectid
    path('viewmark/project/<projectid>/', views.viewmark, name='viewmark'),

    # marking/submit/projectid
    path('checkFormValidity', views.checkFormValidity, name='checkForm'),

    
]
