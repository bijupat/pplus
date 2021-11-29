
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tbllab, Tblinv, Tblrepo, Tbltests, Tblpay, Mstopr
from django.utils.timezone import datetime
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import timedelta

#time delta for 5 hours and 30 min
#TIME_DELTA530 = timedelta(days= 0, hours = 5, minutes = 30)
#declaring users list by oprkey who can verify reports
VERIFY_ALLOWED_USERS = [5]

def index(request):

    # checking if user key is in request.session dict (check if user loged in)
    if 'user' in request.session:

        if request.method == 'GET':
            encounter_today = Tbllab.objects.filter(dor__date=datetime.today().date())
            return render(request, 'report/index.html' , {"encounter" :encounter_today, "index":True,"user":request.session['user']})
    

        if request.method == 'POST':
            date = request.POST["date"]
            encounter_date = Tbllab.objects.filter(dor__date=date)
            return render(request, 'report/index.html', {"encounter" :encounter_date, "index":True, "date" : date, "user":request.session['user']})
            
    else:
        return render(request, "report/login.html", {
                "message": "Please Login."
            })
 


def encounter(request, labkey):

    # checking if user key is in request.session dict (check if user loged in)
    if 'user' in request.session:
    
        # from Verify form from pgrep html 
        if request.method == "POST":
            repokey = request.POST.get('repokey')
            reportpg = Tblrepo.objects.get(pk=repokey)
            labkey = reportpg.labkey.labkey
            reportpg.status = 2
            reportpg.verifydt = datetime.today()
            reportpg.verifyby = request.session['oprkey']
            reportpg.save()
         

            return HttpResponseRedirect(reverse("report:encounter",  args=[labkey]))

        if request.method == "GET":
            e = Tbllab.objects.get(pk=labkey)
            investigation = Tblinv.objects.filter(labkey=labkey)
            p = investigation.all().aggregate(Sum('rate'))
            total = p['rate__sum']
            reports = Tblrepo.objects.filter(labkey=labkey)
            receipts = Tblpay.objects.filter(labkey=labkey)
            x = receipts.all().aggregate(Sum('amount'))
            total_payment = x['amount__sum']            
            if total_payment:
                due = total  - (total_payment + e.disc)
            elif total:
                due = total - e.disc
            else:
                due = -e.disc
            n_disc = 0
            if e.disc:
                n_disc = -e.disc
            # delclairing empty set to pass to template
            payments = []
            # populating payment set with dictionary of reciepts ; userid need diffent implementation 
            for pay in receipts:
                dict= {}
                dict['paidon'] = pay.paidon
                dict['recpno'] = pay.recpno
                dict['amount'] = pay.amount
                dict['userid'] = Mstopr.objects.get(pk=pay.oprkey).oprid
                payments.append(dict)
            can_verify = request.session["oprkey"] in VERIFY_ALLOWED_USERS

       
            return render(request, 'report/encounter.html', {"e" : e, "total": total, "investigations":investigation, "reports":reports, "payments" : payments, "total_payment":total_payment, "due":due, "user":request.session['user'], "n_disc":n_disc,"can_verify":can_verify} )

    else:
        return render(request, "report/login.html", {
                "message": "Please Login."
            })


def reportview(request, labkey):

    if 'user' in request.session:

        if request.method == "GET":
            e = Tbllab.objects.get(pk=labkey)
            reports = Tblrepo.objects.filter(labkey=labkey)
            #repokey_list =[]
            #for report in reports:
            #   repokey_list.append(report.repokey)
            #tests = Tbltests.objects.filter(repokey__in=repokey_list).order_by('repokey', 'eorder')
            repokey_verified_list = []
            for report in reports:
                if report.status > 1:
                    #print(report.status)
                    repokey_verified_list.append(report.repokey)
            #print(repokey_verified_list)
            tests_verified = Tbltests.objects.filter(repokey__in=repokey_verified_list).order_by('repokey', 'eorder')
            #print(tests_verified)


            return render(request, 'report/alltests.html' , {"tests" : tests_verified, "e" : e , "user":request.session['user']})




    else:
        return render(request, "report/login.html", {
            "message": "Please Login."
            })


def editrate(request, invkey):

        if 'user' in request.session:

            if request.method == "POST":
                inv = Tblinv.objects.get(pk=invkey)
                labkey = inv.labkey.labkey
                inv.rate = request.POST.get(inv.item)
                inv.save()


            return HttpResponseRedirect(reverse("report:encounter",  args=[labkey]))

def report(request, repokey):

    # checking if user key is in request.session dict(check if user loged in)
    if 'user' in request.session:

        if request.method == "POST":
            #extracting value from form
            testkey = request.POST.get('testkey')
            newvalue = request.POST.get('result')
            # quering Tbltests table to get test object    
            test = Tbltests.objects.get(testkey=testkey)
            test.result = newvalue            
            test.save()
            print(test.repokey.repokey)
            report = Tblrepo.objects.get(repokey =  test.repokey.repokey)
            report.entryby = request.session['oprkey']
            report.entrydt = datetime.today()
            report.save()
            # getting labkey of the test associated pass to args for reverse
            repokey = test.repokey.repokey

            return HttpResponseRedirect(reverse("report:report",  args=[repokey]))       

        if request.method == "GET":
            #getting tests from paritcular report and odering by eorder fiels of table
            tests_temp = Tbltests.objects.filter(repokey=repokey).order_by('eorder')
            labkey = tests_temp[0].repokey.labkey.labkey
            reporttitle = tests_temp[0].repokey.title
            e = Tbllab.objects.get(pk=labkey)
             #print(request.session["oprkey"])
            can_verify = request.session["oprkey"] in VERIFY_ALLOWED_USERS
            #print(can_verify)
            report = Tblrepo.objects.get(pk=repokey)
            can_enter = False
            if report.status < 2 or can_verify:
                can_enter = True

            #t.test t.result t.testkey t.options
            # populating  dictionary of test ; options  need to  implementated as set
            tests = []
            for t in tests_temp:
                dict={}
                dict['test'] = t.test
                dict['result'] = t.result
                dict['testkey'] = t.testkey
                options= []
                for option in t.options.split('|'):
                    if len(option) > 4:
                        options.append(option)
                dict['options'] = options
                tests.append(dict)
           


            return render(request, 'report/pgrep.html', {"tests" : tests, "e" : e , "reporttitle" :reporttitle, "repokey":repokey, "user":request.session['user'], "can_verify":can_verify, "can_enter":can_enter })
    
    else:
        return render(request, "report/login.html", {
                "message": "Please Login."
            })

def discount (request, labkey):

    if request.method == "POST":
        e = Tbllab.objects.get(pk=labkey)
        e.disc = request.POST.get('addeditdiscountinput')
        e.save()

        return HttpResponseRedirect(reverse("report:encounter",  args=[labkey]))


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
        new_pay = Tblpay.objects.create(labkey=e, paidon = paidon, recpno=recpno, amount=amount, cash = True, printed= False, oprkey = request.session['oprkey'] , paymode = 0)
        
        return HttpResponseRedirect(reverse("report:encounter",  args=[labkey]))


def login_view(request):

    if request.method == "POST":
        #initialise empty USER set
        users=[]
        #Getting all mstopr object with only five colums 'oprkey', 'oprid', 'oprname', 'pw', 'active'
        userobjs = Mstopr.objects.all().values('oprkey', 'oprid', 'oprname', 'pw', 'active')
        #adding users in USERS set
        for user in userobjs:
            users.append(user['oprid'])

        # getting vaues from post form
        username = request.POST["username"]
        password = request.POST["password"]
        #cheking if username in global variable USERS set line 16
        if username in users:
            userobj = Mstopr.objects.filter(oprid=username)
            pw = userobj[0].pw
            # cheking pw and if user is active
            if pw == password and userobj[0].active:
                #appending global variable ACTIVEUSER set with current  validated usreobject
                request.session['user'] = userobj[0].oprname
                request.session['oprkey'] = userobj[0].oprkey
                request.session['userid'] = userobj[0].oprid
                encounter_today = Tbllab.objects.filter(dor__date=datetime.today().date())
                return HttpResponseRedirect(reverse("report:index"))
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

def find(request):
    # checking if user key is in request.session dict(check if user loged in)
    if 'user' in request.session:
        if request.method == "GET":
            return render(request,"report/find.html")

        if request.method == "POST":
            fname = request.POST.get('find_fname')
            lname = request.POST.get("find_lname")
            smpno = request.POST.get("find_smpno")
            mobno = request.POST.get("find_mobno")

            if fname and lname and len(fname)>2 and len(lname)>2:
                date=f"Find F Name '{fname}' and L Name '{lname}'"
                encounter_find = Tbllab.objects.filter(fname__icontains=fname).filter(lname__icontains=lname)
            elif fname and len(fname)>2:
                date=f"Find F Name '{fname}'"
                encounter_find = Tbllab.objects.filter(fname__icontains=fname)
            elif lname and len(lname)>2:
                date=f"Find L Name '{lname}'"
                encounter_find = Tbllab.objects.filter(lname__icontains=lname)   
            elif smpno and int(smpno)>0 and int(smpno)<10000:
                date=f"Find Sample No '{smpno}'"
                encounter_find = Tbllab.objects.filter(sampno=smpno)
            elif mobno and len(mobno) == 10 :
                date=f"Find Mobile no '{mobno}'"
                encounter_find = Tbllab.objects.filter(phone=mobno)
            else:
                return render(request,"report/find.html",{"message":"Invalid Input for Search"})

            return render(request, 'report/index.html', {"encounter" :encounter_find, "date" : date, "user":request.session['user']})
            




def logout_view(request):
    request.session.flush()
    return HttpResponseRedirect(reverse("report:login"))


