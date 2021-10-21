from django.shortcuts import render
from django.http import HttpResponse
from .models import Tbllab, Tblinv, Tblrepo, Tbltests, Tblpay, Tblbills
from django.utils.timezone import datetime
from django.db.models import Sum, Max
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import timedelta

TIME_DELTA530 = timedelta(days= 0, hours = 5, minutes = 30)


def index(request):
    if request.method == 'GET':
        #date format (yyyy,mm,dd)
        encounter_today = Tbllab.objects.filter(dor__date=datetime.today().date())
        return render(request, 'report\index.html', {"encounter" :encounter_today})

    elif request.method == 'POST':
        date = request.POST["date"]
        encounter_date = Tbllab.objects.filter(dor__date=date)
        return render(request, 'report\index.html', {"encounter" :encounter_date, "date" : date})

    
def encounter(request, labkey):
    if request.method == "POST":
        repokey = request.POST.get('repokey')
        reportpg = Tblrepo.objects.get(pk=repokey)
        labkey = reportpg.labkey.labkey
        reportpg.status = 2
        reportpg.verifydt = datetime.today() + + TIME_DELTA530
        reportpg.verifyby = 5
        reportpg.save()

        return HttpResponseRedirect(reverse("encounter",  args=[labkey]))

    else:
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

        return render(request, 'report\encounter.html', {"e" : e, "total": total, "investigations":investigation, "reports":reports, "payments" : payments, "total_payment":total_payment, "due":due } )

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

        return render(request, 'report\pgrep.html', {"tests" : tests, "e" : e , "reporttitle" :reporttitle, "repokey":repokey })
    
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

