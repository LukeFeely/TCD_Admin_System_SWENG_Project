'''
This is a class for mapping out what data is needed from each of the different form types designed for each course.

'''

from django import forms
from marking.models import ICSProjectModel, ICSProjectModelDraft, PDF

class ICSProjectForm(forms.ModelForm):
	class Meta:
		model = ICSProjectModel
		fields = "__all__"

class ICSProjectFormDraft(forms.ModelForm):
	class Meta:
		model = ICSProjectModelDraft
		fields = "__all__"


class PDFForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ('file', )