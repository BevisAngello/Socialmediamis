from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db import models

from django.db.models import *

from SocialMediaThreats.forms import ThreatForm
from SocialMediaThreats.forms import TechniquesForm
from SocialMediaThreats.forms import CreateUserForm
from SocialMediaThreats.forms import AwarenessForm
from SocialMediaThreats.models import Threats
from SocialMediaThreats.models import Awareness
from SocialMediaThreats.models import Techniques

# from SocialMediaThreats.models import HistoricalTechniques
# from SocialMediaThreats.models import easyaudit_loginevent
# from .models import easyaudit_requestevent
from easyaudit.models import CRUDEvent, LoginEvent, RequestEvent


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.db.models.functions import Extract


from SocialMediaThreats.filters import ThreatsFilter, MonthlyFilter

# from SocialMediaThreats.decorators import unauthenticated_user, allowed_users
from SocialMediaThreats.decorators import unauthenticated_user

import datetime


def addthreat(request):
    if request.method == "POST":
        form = ThreatForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/viewthreat')
            except:
                pass
    else:
        form=ThreatForm()
    return render(request,'addthreat.html',{'form':form})

def techniques(request):
    if request.method == "POST":
        form = TechniquesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/viewtechnique')
            except:
                pass
    else:
        form=TechniquesForm()
    return render(request,'techniques.html',{'form':form})

def awareness(request):
    if request.method == "POST":
        form = AwarenessForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/viewawareness')
            except:
                pass
    else:
        form=AwarenessForm()
    return render(request,'awareness.html',{'form':form})


def Reportthreat(request):
    if request.method == "POST":
        form = ThreatForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/viewthreat')
            except:
                pass
    else:
        form=ThreatForm()
    return render(request,'Reportthreat.html',{'form':form})

def Reporttechnique(request):
    if request.method == "POST":
        form = TechniquesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/viewtechnique')
            except:
                pass
    else:
        form=TechniquesForm()
    return render(request,'Reporttechnique.html',{'form':form})

def Reportawareness(request):
    if request.method == "POST":
        form = AwarenessForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/viewawareness')
            except:
                pass
    else:
        form=AwarenessForm()
    return render(request,'Reportawareness.html',{'form':form})

def edittechnique(request, id):  
    techniques = Techniques.objects.get(id=id)  
    form = TechniquesForm(request.POST, instance = techniques)  
    if form.is_valid():  
        form.save()  
        return redirect("/viewtechnique")  
    return render(request, 'edittechnique.html', {'techniques':techniques})  

# def edittechnique(request, id=0):
#     if request.method == "GET":
#         if id==0:
#             form = TechniquesForm()
#         else:
#             techniques = Techniques.objects.get(pk=id)
#             form = TechniquesForm(instance= techniques)
#         return render(request,'edittechnique.html', {'techniques':techniques})
#     else:
#         if id==0:
#             form = TechniquesForm(instance= techniques)
#         else:
#             techniques = Techniques.objects.get(pk=id)
#             form = TechniquesForm(request.POST, instance= techniques)
#         if form.is_valid():
#             form.save()
#         return redirect('/viewtechnique')



def editthreat(request, id=0):
    # SocialMediaThreats = Threats.objects.get(id=id)
    if request.method == "GET":
        if id==0:
            form = ThreatForm()
        else:
            threats = Threats.objects.get(pk=id)
            form = ThreatForm(instance= threats)
        return render(request,'editthreat.html', {'threats':threats})
    else:
        if id==0:
            form = ThreatForm(request.POST)
        else:
            threats = Threats.objects.get(pk=id)
            form=ThreatForm(request.POST, instance= threats)
        if form.is_valid():
            form.save()
        return redirect('/viewthreat')


# def edittechnique(request, id=0):
#     # SocialMediaThreats = Threats.objects.get(id=id)
#     if request.method == "GET":
#         if id==0:
#             form = TechniquesForm()
#         else:
#             techniques = Techniques.objects.get(pk=id)
#             form = TechniquesForm(instance= techniques)
#         return render(request,'edittechnique.html', {'techniques':techniques})
#     else:
#         if id==0:
#             form = TechniquesForm(request.POST)
#         else:
#             techniques = Techniques.objects.get(pk=id)
#             form=TechniquesForm(request.POST, instance= techniques)
#         if form.is_valid():
#             form.save()
#         return redirect('/viewtechnique')

def editawareness(request, id=0):
    # SocialMediaThreats = Threats.objects.get(id=id)
    if request.method == "GET":
        if id==0:
            form = AwarenessForm()
        else:
            awareness = Awareness.objects.get(pk=id)
            form = AwarenessForm(instance= awareness)
        return render(request,'editawareness.html', {'awareness':awareness})
    else:
        if id==0:
            form = AwarenessForm(request.POST)
        else:
            awareness = Awareness.objects.get(pk=id)
            form=AwarenessForm(request.POST, instance= awareness)
        if form.is_valid():
            form.save()
        return redirect('/viewawareness')

            

@login_required(login_url='/loginPage')
# @allowed_users(allowed_roles=['administrator', 'user'])
def dashboard(request):
    # Student = Students.objects.all()
    threats = Threats.objects.all()
    techniques = Techniques.objects.all()
    awareness = Awareness.objects.all()

    
    total_threats = threats.count()
    total_techniques = techniques.count()
    total_awareness = awareness.count()

    total_Electronic_fraud = Threats.objects.filter(typeofsocialmediacrime='Electronic fraud').count()
    total_Cyber_harassment = Threats.objects.filter(typeofsocialmediacrime='Cyber harassment').count()
    total_Revenge_porn = Threats.objects.filter(typeofsocialmediacrime='Revenge porn').count()
    total_Cyber_stalking = Threats.objects.filter(typeofsocialmediacrime='Cyber stalking').count()
    total_Phishing = Threats.objects.filter(typeofsocialmediacrime='Phishing').count()

    total_Radio_Ads = Awareness.objects.filter(typeofawareness='Radio Ads').count()
    total_Television = Awareness.objects.filter(typeofawareness='Television').count()
    total_Social_media_Influencing = Awareness.objects.filter(typeofawareness='Social media Influencing').count()
    total_Cyber_education = Awareness.objects.filter(typeofawareness='Cyber education').count()
    total_Phishing_Awareness = Awareness.objects.filter(typeofawareness='Phishing_Awareness').count()


    context = {'threats':threats, 'techniques':techniques,'awareness':awareness,
	'total_threats':total_threats,'total_techniques':total_techniques,
	'total_awareness':total_awareness, 
    'total_Electronic_fraud':total_Electronic_fraud, 'total_Cyber_harassment':total_Cyber_harassment,
    'total_Revenge_porn':total_Revenge_porn, 'total_Cyber_stalking':total_Cyber_stalking,
    'total_Phishing':total_Phishing ,
    'total_Radio_Ads':total_Radio_Ads, 'total_Television':total_Television,
    'total_Social_media_Influencing':total_Social_media_Influencing, 'total_Cyber_education':total_Cyber_education,
    'total_Phishing_Awareness':total_Phishing_Awareness}


    return render(request,"dashboard.html", context)

def beforelogindashboard(request):

    threats = Threats.objects.all()
    techniques = Techniques.objects.all()
    awareness = Awareness.objects.all()

    total_threats = threats.count()
    total_techniques = techniques.count()
    total_awareness = awareness.count()

    total_Electronic_fraud = Threats.objects.filter(typeofsocialmediacrime='Electronic fraud').count()
    total_Cyber_harassment = Threats.objects.filter(typeofsocialmediacrime='Cyber harassment').count()
    total_Revenge_porn = Threats.objects.filter(typeofsocialmediacrime='Revenge porn').count()
    total_Cyber_stalking = Threats.objects.filter(typeofsocialmediacrime='Cyber stalking').count()
    total_Phishing = Threats.objects.filter(typeofsocialmediacrime='Phishing').count()

    total_Radio_Ads = Awareness.objects.filter(typeofawareness='Radio Ads').count()
    total_Television = Awareness.objects.filter(typeofawareness='Television').count()
    total_Social_media_Influencing = Awareness.objects.filter(typeofawareness='Social media Influencing').count()
    total_Cyber_education = Awareness.objects.filter(typeofawareness='Cyber education').count()
    total_Phishing_Awareness = Awareness.objects.filter(typeofawareness='Phishing_Awareness').count()


    context = {'threats':threats, 'techniques':techniques,'awareness':awareness,
	'total_threats':total_threats,'total_techniques':total_techniques,
	'total_awareness':total_awareness,
    'total_Electronic_fraud':total_Electronic_fraud, 'total_Cyber_harassment':total_Cyber_harassment,
    'total_Revenge_porn':total_Revenge_porn, 'total_Cyber_stalking':total_Cyber_stalking,
    'total_Phishing':total_Phishing ,
    'total_Radio_Ads':total_Radio_Ads, 'total_Television':total_Television,
    'total_Social_media_Influencing':total_Social_media_Influencing, 'total_Cyber_education':total_Cyber_education,
    'total_Phishing_Awareness':total_Phishing_Awareness}

    return render(request,"beforelogindashboard.html", context)

class threatreporting(TemplateView):
    template_name = 'threatreporting.html'

def Analysis(request):
    # Student = Students.objects.all()
    #  return render(request,"home.html",{'Student':Student})
     return render(request,"Analysis.html")

# @login_required(login_url="/loginPage")
def viewthreat(request):
    # SocialMediaThreats = Threats.objects.all()
    threats = Threats.objects.all()
    # return render(request,"viewthreat.html",{'SocialMediaThreats':SocialMediaThreats})
    myFilter = ThreatsFilter(request.GET, queryset=threats)
    threats = myFilter.qs

    context = {'myFilter':myFilter, 'threats':threats}

    return render(request,"viewthreat.html",context)

# @login_required(login_url="/loginPage")
# def viewthreat(request):
#     # SocialMediaThreats = Threats.objects.all()
#     threats = Threats.objects.all()
#     # return render(request,"viewthreat.html",{'SocialMediaThreats':SocialMediaThreats})
#     myFilter = ThreatsFilter(request.GET, queryset=SocialMediaThreats)
#     SocialMediaThreats = myFilter.qs

#     context = {'myFilter':myFilter, 'SocialMediaThreats':SocialMediaThreats, 'threats':threats}

#     return render(request,"viewthreat.html",context)

def viewtechnique(request):
    techniques = Techniques.objects.all()

    context = {'techniques':techniques }
    return render(request,"viewtechnique.html",context)

def viewawareness(request):
    awareness = Awareness.objects.all()
    context = {'awareness':awareness }
    return render(request,"viewawareness.html",context)

def monthlyanalysis(request):
    SocialMediaThreats = Threats.objects.all()
    # SocialMediaThreats = Awareness.objects.all()
    # return render(request,"monthlyanalysis.html",{'SocialMediaThreats':SocialMediaThreats})
    # Sample.objects.filter(date__year='2020', date__month='01')
    month = Threats.objects.filter().extra({'month':"Extract(month from date_created_threat)"}).values_list('month').annotate(Count('id'))
    # month = Threats.objects.annotate(month_stamp=Extract('date_created_threat', 'month')).values_list('month_stamp', flat=True)

    # April = monthreported.
    April = Threats.objects.filter(typeofsocialmediacrime='Electronic fraud').count()
    myFilter = MonthlyFilter(request.GET, queryset=SocialMediaThreats)
    SocialMediaThreats = myFilter.qs

    context = {'myFilter':myFilter, 'SocialMediaThreats':SocialMediaThreats,'month':month, 'April':April}

    return render(request,"monthlyanalysis.html",context)
    # return render(request,"monthlyanalysis.html",{'SocialMediaThreats':SocialMediaThreats},context)

# @allowed_users(allowed_roles=['administrator', 'user'])
def annualanalysis(request):
    SocialMediaThreats = Awareness.objects.all()
    return render(request,"annualanalysis.html",{'SocialMediaThreats':SocialMediaThreats})

@login_required(login_url='/loginPage')
# @allowed_users(allowed_roles=['administrator'])
def help(request):
    # SocialMediaThreats = SocialMediaThreats.objects.all()
    return render(request,"help.html")

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('beforelogindashboard')

@unauthenticated_user   
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('/loginPage')
    #         try:
    #             form.save()
    #             return redirect('/login')
    #         except:
    #             pass
    # else:
    context = {'form':form}
    return render(request, 'register.html', context)

# def viewHistoricalTechniques(request):
#     historicaltechniques = HistoricalTechniques.objects.all()

#     context = {'historicaltechniques':historicaltechniques }
#     return render(request,"Audittrail.html",context)

@login_required(login_url='/loginPage')
# @allowed_users(allowed_roles=['administrator'])
def AuditTrail(request):
    requestevent = RequestEvent.objects.all()
    loginevent = LoginEvent.objects.all()

    context = {'requestevent':requestevent,'loginevent':loginevent }
    return render(request,"Audittrail.html",context)
