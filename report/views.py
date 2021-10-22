
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tbllab, Tblinv, Tblrepo, Tbltests, Tblpay, Mstopr
from django.utils.timezone import datetime
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import timedelta
from django.db import IntegrityError

#time delta for 5 hours and 30 min
TIME_DELTA530 = timedelta(days= 0, hours = 5, minutes = 30)
#initialise empty USER set
USERS=[]
#Getting all mstopr object with only five colums 'oprkey', 'oprid', 'oprname', 'pw', 'active'
USEROBJS = Mstopr.objects.all().values('oprkey', 'oprid', 'oprname', 'pw', 'active')
#adding users in USERS set
for USER in USEROBJS:
    USERS.append(USER['oprid'])
ACTIVEUSER =[]

def index(request):
    if request.method == 'GET' and ACTIVEUSER:
        encounter_today = Tbllab.objects.filter(dor__date=datetime.today().date())
        return render(request, 'report/index.html' , {"encounter" :encounter_today, "user":ACTIVEUSER[0][0]})
 

    elif request.method == 'POST' and ACTIVEUSER:
        date = request.POST["date"]
        encounter_date = Tbllab.objects.filter(dor__date=date)
        return render(request, 'report\index.html', {"encounter" :encounter_date, "date" : date, "user":ACTIVEUSER[0][0]})
        
    else:
        return render(request, "report/login.html", {
                "message": "Please Login."
            })
 


def encounter(request, labkey):
    if request.method == "POST" and ACTIVEUSER:
        repokey = request.POST.get('repokey')
        reportpg = Tblrepo.objects.get(pk=repokey)
        labkey = reportpg.labkey.labkey
        reportpg.status = 2
        reportpg.verifydt = datetime.today() + + TIME_DELTA530
        reportpg.verifyby = 5
        reportpg.save()

        return HttpResponseRedirect(reverse("encounter",  args=[labkey]))

    elif request.method == "GET" and ACTIVEUSER:
        e = Tbllab.objects.get(pk=labkey)
        investigation = Tblinv.objects.filter(labkey=labkey)
        p = investigation.all().aggregate(Sum('rate'))
        total = p['rate__sum']
        reports = Tblrepo.objects.filter(labkey=labkey)
        payments = Tblpay.objects.filter(labkey=labkey)
        x = payments.all().aggregate(Sum('amount'))
        total_payment = x['amount__sum']
        if total_payment:
            due = total  - (int(total_payment) + int(e.disc))
        else:
            due = 0       
        print(ACTIVEUSER[0])
        return render(request, 'report\encounter.html', {"e" : e, "total": total, "investigations":investigation, "reports":reports, "payments" : payments, "total_payment":total_payment, "due":due, "user":ACTIVEUSER[0][0] } )

    else:
        return render(request, "report/login.html", {
                "message": "Please Login."
            })

def report(request, repokey):

    if request.method == "POST":
        #extracting value from form
        testkey = request.POST.get('testkey')
        newvalue = request.POST.get('result')
        # quering Tbltests table to get test object    
        test = Tbltests.objects.get(testkey=testkey)
        test.result = newvalue
        test.save()
        # getting labkey of the test associated pass to args for reverse
        repokey = test.repokey.repokey

        return HttpResponseRedirect(reverse("report",  args=[repokey]))       

    else:
        tests = Tbltests.objects.filter(repokey=repokey)
        labkey = tests[0].repokey.labkey.labkey
        reporttitle = tests[0].repokey.title
        e = Tbllab.objects.get(pk=labkey)

        return render(request, 'report\pgrep.html', {"tests" : tests, "e" : e , "reporttitle" :reporttitle, "repokey":repokey,"user":ACTIVEUSER[0][0] })


def discount (request, labkey):

    if request.method == "POST":
        e = Tbllab.objects.get(pk=labkey)
        e.disc = request.POST.get('addeditdiscountinput')
        e.save()

        return HttpResponseRedirect(reverse("encounter",  args=[labkey]))


def addpayment (request, labkey):
    if request.method == "POST":
        #getting latest Tblpay object sorted by paidon field lookup for recpno field
        #model will automatically increment latest recpno
        recpno = Tblpay.objects.latest('paidon').recpno     
        # getting instance of Tbllab for labkey field in Tblpay
        e = Tbllab.objects.get(labkey=labkey)
        paidon = datetime.today()
        #extracting value from form
        amount = request.POST.get('addpayment')
        #create new Tblpay object instance
        new_pay = Tblpay.objects.create(labkey=e, paidon = paidon, recpno=recpno, amount=amount, cash = True, printed= False, oprkey = 5, paymode = 0)
        
        return HttpResponseRedirect(reverse("encounter",  args=[labkey]))


def login_view(request):
    if request.method == "POST":

        # getting vaues from post form
        username = request.POST["username"]
        password = request.POST["password"]
        #cheking if username in global variable USERS set line 16
        if username in USERS:
            userobj = Mstopr.objects.filter(oprid=username)
            pw = userobj[0].pw
            # cheking pw and if user is active
            if pw == password and userobj[0].active:
                #appending global variable ACTIVEUSER set with current  validated usreobject
                ACTIVEUSER.append(userobj)
                encounter_today = Tbllab.objects.filter(dor__date=datetime.today().date())
                return render(request, 'report/index.html' , {"encounter" :encounter_today, "user":userobj[0]})
            else:
                return render(request, "report/login.html", {
                "message": "Invalid Password."
            })
        else:
                return render(request, "report/login.html", {
                "message": "Invalid Username."
            })
    else:
        return render(request, "report/login.html")


def logout_view(request):
    ACTIVEUSER=[]
    return HttpResponseRedirect(reverse("login"))

