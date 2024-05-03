
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tbllab, Tblinv, Tblrepo, Tbltests, Tblpay, Mstopr
from django.utils.timezone import datetime
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import timedelta
import csv, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#time delta for 5 hours and 30 min  
#TIME_DELTA530 = timedelta(days= 0, hours = 5, minutes = 30)
#declaring users list by oprkey who can verify reports
VERIFY_ALLOWED_USERS = [5]

def discountlist(request):
    USERDB = request.session['dbname']
# checking if user key is in request.session dict (check if user loged in)
    if 'user' in request.session:
        if request.method == 'GET':
            encs = Tbllab.objects.using(USERDB).order_by('-dor').filter(disc__gt = 0)[0:50]
        return render(request, 'report/index.html' , {"encounter" :encs, "index":False})

def paymentupdate(request, oprkey):
    USERDB = request.session['dbname']
# checking if user key is in request.session dict (check if user loged in)
    if 'user' in request.session:
        if request.method == 'GET':
            if oprkey == 0:
                receipts = Tblpay.objects.using(USERDB).filter(cash = True).order_by('-paidon').exclude(oprkey=5).filter(paidon__year__gte = 2022)[0:50]
            elif oprkey == 100000:
                receipts = Tblpay.objects.using(USERDB).filter(cash = False).order_by('-paidon').exclude(oprkey=5).filter(paidon__year__gte = 2022)[0:50]            
            else:         
                receipts = Tblpay.objects.using(USERDB).filter(cash = True).order_by('-paidon').filter(oprkey=oprkey).filter(paidon__year__gte = 2022)[0:50]

            return render(request, 'report/paymentupdate.html', {"receipts" : receipts, "oprkey": oprkey})

        if request.method == 'POST':
            # receipt.paykey is passed from template as oprkey
            paymentobject = Tblpay.objects.using(USERDB).get(pk=request.POST["receipt_paykey"])
            #first save paymentobject.userkey in userkey before it gets changed
            # now change payment object user (oprkey) and save it
            paymentobject.oprkey = request.session['oprkey']
            # change payment paidon if passed in form
            date = request.POST["date"]
            if date : 
                paymentobject.paidon = date
                print(True)
            else:
                print(False)
            paymentobject.save()

            return HttpResponseRedirect(reverse("report:paymentupdate",  args=[oprkey]))
            
    else:
        return render(request, "report/login.html", {
                "message": "Please Login."
            })

def index(request):
    # checking if user key is in request.session dict (check if user loged in)
    if 'user' in request.session:
        USERDB = request.session['dbname']
        # host = request.get_host()
        if request.method == 'GET':
            encounter_today = Tbllab.objects.using(USERDB).filter(dor__date=datetime.today().date())

            #print(encounter_today.values().first())
            return render(request, 'report/index.html' , {"encounter" :encounter_today, "index":True})
    

        if request.method == 'POST':
            date = request.POST["date"]
            encounter_date = Tbllab.objects.using(USERDB).filter(dor__date=date)

            return render(request, 'report/index.html', {"encounter" :encounter_date, "index":True, "date" : date, "user":request.session['user']})
            
    else:
        return render(request, "report/login.html", {
                "message": "Please Login."
            })
 


def encounter(request, labkey):

    # checking if user key is in request.session dict (check if user loged in)
    if 'user' in request.session:
        USERDB = request.session['dbname']
        # from Verify form from pgrep html 
        if request.method == "POST":
            repokey = request.POST.get('repokey')
            reportpg = Tblrepo.objects.using(USERDB).get(pk=repokey)
            labkey = reportpg.labkey.labkey
            reportpg.status = 2
            reportpg.verifydt = datetime.today()
            reportpg.verifyby = request.session['oprkey']
            reportpg.save()
         

            return HttpResponseRedirect(reverse("report:encounter",  args=[labkey]))

        if request.method == "GET":
            e = Tbllab.objects.using(USERDB).get(pk=labkey)
            investigation = Tblinv.objects.using(USERDB).filter(labkey=labkey)
            p = investigation.all().aggregate(Sum('rate'))
            total = p['rate__sum']
            reports = Tblrepo.objects.using(USERDB).filter(labkey=labkey)
            receipts = Tblpay.objects.using(USERDB).filter(labkey=labkey)
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
                dict['userid'] = Mstopr.objects.using(USERDB).get(pk=pay.oprkey).oprid
                payments.append(dict)
            can_verify = request.session["oprkey"] in VERIFY_ALLOWED_USERS

       
            return render(request, 'report/encounter.html', {"e" : e, "total": total, "investigations":investigation, "reports":reports, "payments" : payments, "total_payment":total_payment, "due":due, "n_disc":n_disc,"can_verify":can_verify} )

    else:
        return render(request, "report/login.html", {
                "message": "Please Login."
            })


def reportview(request, labkey):

    if 'user' in request.session:
        USERDB = request.session['dbname']
        if request.method == "GET":
            e = Tbllab.objects.using(USERDB).get(pk=labkey)
            reports = Tblrepo.objects.using(USERDB).filter(labkey=labkey)
            #repokey_list =[]
            #for report in reports:
            #   repokey_list.append(report.repokey)
            #tests = Tbltests.objects.using(USERDB).filter(repokey__in=repokey_list).order_by('repokey', 'eorder')
            repokey_verified_list = []
            for report in reports:
                if report.status > 1:
                    repokey_verified_list.append(report.repokey)
            tests_verified = Tbltests.objects.using(USERDB).filter(repokey__in=repokey_verified_list).order_by('repokey', 'eorder')
            #print(tests_verified.values())
            #print(e.refdr.mobile)
            return render(request, 'report/alltests.html' , {"tests" : tests_verified, "e" : e })




    else:
        return render(request, "report/login.html", {
            "message": "Please Login."
            })


def editrate(request, invkey):

        if 'user' in request.session:
            USERDB = request.session['dbname']
            if request.method == "POST":
                inv = Tblinv.objects.using(USERDB).get(pk=invkey)
                labkey = inv.labkey.labkey
                inv.rate = request.POST.get(inv.item)
                inv.save()
            return HttpResponseRedirect(reverse("report:encounter",  args=[labkey]))

def report(request, repokey):

    # checking if user key is in request.session dict(check if user loged in)
    if 'user' in request.session:
        USERDB = request.session['dbname']
        if request.method == "POST":
            #extracting value from form
            testkey = request.POST.get('testkey')
            newvalue = request.POST.get('result')
            # quering Tbltests table to get test object    
            test = Tbltests.objects.using(USERDB).get(testkey=testkey)
            test.result = newvalue            
            test.save()
            report = Tblrepo.objects.using(USERDB).get(repokey =  test.repokey.repokey)
            report.entryby = request.session['oprkey']
            report.entrydt = datetime.today()
            report.save()
            # getting labkey of the test associated pass to args for reverse
            repokey = test.repokey.repokey

            return HttpResponseRedirect(reverse("report:report",  args=[repokey]))       

        if request.method == "GET":
            #getting tests from paritcular report and odering by eorder fiels of table
            tests_temp = Tbltests.objects.using(USERDB).filter(repokey=repokey).order_by('eorder')
            labkey = tests_temp[0].repokey.labkey.labkey
            reporttitle = tests_temp[0].repokey.title
            e = Tbllab.objects.using(USERDB).get(pk=labkey)
            can_verify = request.session["oprkey"] in VERIFY_ALLOWED_USERS
            report = Tblrepo.objects.using(USERDB).get(pk=repokey)
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
           


            return render(request, 'report/pgrep.html', {"tests" : tests, "e" : e , "reporttitle" :reporttitle, "repokey":repokey, "can_verify":can_verify, "can_enter":can_enter })
    
    else:
        return render(request, "report/login.html", {
                "message": "Please Login."
            })

def discount (request, labkey):

    if request.method == "POST":
        USERDB = request.session['dbname']
        e = Tbllab.objects.using(USERDB).get(pk=labkey)
        e.disc = request.POST.get('addeditdiscountinput')
        e.save()

        return HttpResponseRedirect(reverse("report:encounter",  args=[labkey]))


def addpayment (request, labkey):
    
    if request.method == "POST":
        USERDB = request.session['dbname']
        #getting latest Tblpay object sorted by paidon field lookup for recpno field
        #model will automatically increment latest recpno
        recpno = Tblpay.objects.using(USERDB).latest('paidon').recpno     
        # getting instance of Tbllab for labkey field in Tblpay
        e = Tbllab.objects.using(USERDB).get(labkey=labkey)
        paidon = datetime.today()
        #extracting value from form
        amount = request.POST.get('addpayment')
        #create new Tblpay object instance
        new_pay = Tblpay.objects.using(USERDB).create(labkey=e, paidon = paidon, recpno=recpno, amount=amount, cash = True, printed= False, oprkey = request.session['oprkey'] , paymode = 0)
        
        return HttpResponseRedirect(reverse("report:encounter",  args=[labkey]))


def login_view(request):

    if request.method == "POST":
        # getting vaues from post form
        username = request.POST["username"]
        password = request.POST["password"]
        USERDB = request.POST['dbname']
        #initialise empty USER set
        users=[]
        #Getting all mstopr object with only five colums 'oprkey', 'oprid', 'oprname', 'pw', 'active'
        # using repr(str(USERDB)) converted variable in 'variable'
        userobjs = Mstopr.objects.using(USERDB).using(USERDB).all().values('oprkey', 'oprid', 'oprname', 'pw', 'active')
        #adding users in USERS set
        for user in userobjs:
            users.append(user['oprid'])

        if username in users:
            userobj = Mstopr.objects.using(USERDB).using(USERDB).filter(oprid=username)
            pw = userobj[0].pw
            
            # cheking pw and if user is active
            if pw == password and userobj[0].active:
                #Setting session values with current user credentials
                request.session['user'] = userobj[0].oprname
                request.session['oprkey'] = userobj[0].oprkey
                request.session['userid'] = userobj[0].oprid
                request.session['dbname'] = USERDB
                
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
        USERDB = request.session['dbname']
        if request.method == "GET":
            return render(request,"report/find.html", {"user":request.session['user']})

        if request.method == "POST":
            fname = request.POST.get('find_fname')
            lname = request.POST.get("find_lname")
            smpno = request.POST.get("find_smpno")
            mobno = request.POST.get("find_mobno")

            if fname and lname and len(fname)>2 and len(lname)>2:
                date=f"Find F Name '{fname}' and L Name '{lname}'"
                encounter_find = Tbllab.objects.using(USERDB).filter(fname__icontains=fname).filter(lname__icontains=lname).order_by('-dor')
            elif fname and len(fname)>2:
                if not lname:
                    date=f"Find F Name '{fname}'"
                    encounter_find = Tbllab.objects.using(USERDB).filter(fname__icontains=fname).order_by('-dor')
                else:
                    return render(request,"report/find.html",{"message":"Please Search L name by 3 or more characters"}) 
            elif lname and len(lname)>2:
                if not fname:
                    date=f"Find L Name '{lname}'"
                    encounter_find = Tbllab.objects.using(USERDB).filter(lname__icontains=lname).order_by('-dor')
                else:
                    return render(request,"report/find.html",{"message":"Please Search F name by 3 or more characters"})  
            elif smpno and int(smpno)>0 and int(smpno)<10000:
                date=f"Find Sample No '{smpno}'"
                encounter_find = Tbllab.objects.using(USERDB).filter(sampno=smpno)
            elif mobno and len(mobno) == 10 :
                date=f"Find Mobile no '{mobno}'"
                encounter_find = Tbllab.objects.using(USERDB).filter(phone=mobno)
            else:
                return render(request,"report/find.html",{"message":"Invalid Input for Search"})

            return render(request, 'report/index.html', {"encounter" :encounter_find, "date" : date, "user":request.session['user']})
            
def logout_view(request):
    request.session.flush()
    request.session.clear()
    return HttpResponseRedirect(reverse("report:login"))


def get_price(request):
    if request.method == "POST":
        pass    
    context = []
    with open(os.path.join(BASE_DIR,'pricelist.csv')) as file:
        reader = csv.DictReader(file)
        for row in reader:
            context.append(row)
    # print(context)
    return render(request, 'report/get_price.html', {'context' : context})