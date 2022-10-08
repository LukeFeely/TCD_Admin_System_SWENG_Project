from django.shortcuts import render


def login(request):
    return render(request, 'SoftwareEngineeringProject/login.html')

def loginredirect(request):
	    return render(request, 'SoftwareEngineeringProject/loginredirect.html')