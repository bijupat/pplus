from django.shortcuts import render
from django.http import HttpResponse

def index(request):                
    return render(request, 'myweb/index.html')
 
def user_defined(request):
    return render(request, 'myweb/user_defined.html')
 
def appdev(request):
    return render(request, 'myweb/appdev.html')
 
def intauto(request):
    return render(request, 'myweb/intauto.html')

def workimp(request):
    return render(request, 'myweb/workimp.html')

def telehealth(request):
    return render(request, 'myweb/telehealth.html')

def website(request):
    return render(request, 'myweb/website.html')

def qa(request):
    return render(request, 'myweb/qa.html')


def promotor(request):
    return render(request, 'myweb/error.html')
        

def coreteam(request):
    return render(request, 'myweb/error.html')
        
def inquiry(request):
    return render(request, 'myweb/inquiry.html')
        
def contactus(request):
    return render(request, 'myweb/contactus.html')