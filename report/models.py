# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class ClientLab(models.Model):
    name = models.CharField(max_length=100)
    schema_name = models.CharField(max_length=20)
    created_on = models.DateField(auto_now_add=True)
    paid_until =  models.DateField()
    on_trial = models.BooleanField(default=True)
    host = models.CharField(max_length=50, blank=True, null=True)

    # default true, schema will be automatically created and synced when it is saved
    #auto_create_schema = True

    class Meta:
        managed = False
        db_table = 'ClientLab'


class Client(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=128)
    ClientLab = models.ForeignKey(ClientLab, models.PROTECT)

    class Meta:
        managed = False
        db_table = 'Userlab'
    
class Bedmaster(models.Model):
    bedid = models.BigIntegerField(db_column='BedId')  # Field name made lowercase.
    bedcode = models.CharField(db_column='BedCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    roomid = models.BigIntegerField(db_column='RoomId', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
    occupied = models.BooleanField(db_column='Occupied', blank=True, null=True)  # Field name made lowercase.
    inactive = models.BooleanField(db_column='InActive', blank=True, null=True)  # Field name made lowercase.
    serviceid = models.BigIntegerField(db_column='ServiceId', blank=True, null=True)  # Field name made lowercase.
    extno = models.CharField(db_column='ExtNo', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BedMaster'


class Roommaster(models.Model):
    roomid = models.BigIntegerField(db_column='RoomId')  # Field name made lowercase.
    roomcode = models.CharField(db_column='RoomCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wardid = models.BigIntegerField(db_column='WardId', blank=True, null=True)  # Field name made lowercase.
    inactive = models.BooleanField(db_column='Inactive', blank=True, null=True)  # Field name made lowercase.
    floorid = models.BigIntegerField(db_column='FloorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoomMaster'


class Samplefrom(models.Model):
    sr_no = models.CharField(db_column='Sr No', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wardname = models.CharField(db_column='WARDNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bedno = models.CharField(db_column='BEDNO', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SAMPLEFROM'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dtproperties(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)


class Logdeletes(models.Model):
    logpk = models.AutoField(db_column='logPk', primary_key=True)  # Field name made lowercase.
    logdate = models.DateTimeField(db_column='logDate')  # Field name made lowercase.
    rectype = models.CharField(db_column='RecType', max_length=15)  # Field name made lowercase.
    trnno = models.IntegerField(db_column='TrnNo')  # Field name made lowercase.
    trndate = models.DateTimeField(db_column='TrnDate')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.
    labrefno = models.CharField(db_column='LabRefNo', max_length=17)  # Field name made lowercase.
    patname = models.CharField(db_column='PatName', max_length=62)  # Field name made lowercase.
    compname = models.CharField(db_column='CompName', max_length=15)  # Field name made lowercase.
    accname = models.CharField(db_column='AccName', max_length=40)  # Field name made lowercase.
    oprid = models.CharField(db_column='OPRID', max_length=5)  # Field name made lowercase.
    delreason = models.CharField(db_column='DelReason', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logDeletes'


class Loglogins(models.Model):
    logpk = models.BigAutoField(db_column='PK', primary_key=True)  # Field name made lowercase.
    login = models.DateTimeField(db_column='LogIn')  # Field name made lowercase.
    logout = models.DateTimeField(db_column='LogOut', blank=True, null=True)  # Field name made lowercase.
    oprid = models.CharField(db_column='OPRID', max_length=5)  # Field name made lowercase.
    compname = models.CharField(db_column='CompName', max_length=16)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logLogins'


class Logresultaudit(models.Model):
    labkey = models.IntegerField(db_column='LabKey')  # Field name made lowercase.
    testkey = models.IntegerField(db_column='TestKey')  # Field name made lowercase.
    oldresult = models.CharField(db_column='OldResult', max_length=180)  # Field name made lowercase.
    newresult = models.CharField(db_column='NewResult', max_length=180)  # Field name made lowercase.
    oldentryby = models.CharField(db_column='OldEntryBy', max_length=5)  # Field name made lowercase.
    oldverifyby = models.CharField(db_column='OldVerifyBy', max_length=5)  # Field name made lowercase.
    oldentrydate = models.DateTimeField(db_column='OldEntryDate')  # Field name made lowercase.
    oldverifydate = models.DateTimeField(db_column='OldVerifyDate', blank=True, null=True)  # Field name made lowercase.
    editedby = models.CharField(db_column='EditedBy', max_length=5)  # Field name made lowercase.
    editmode = models.CharField(db_column='EditMode', max_length=1)  # Field name made lowercase.
    editdate = models.DateTimeField(db_column='EditDate')  # Field name made lowercase.
    compname = models.CharField(db_column='CompName', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logResultAudit'


class Mst2Incent(models.Model):
    incentpk = models.AutoField(db_column='IncentPk', primary_key=True)  # Field name made lowercase.
    incent2name = models.CharField(db_column='Incent2Name', unique=True, max_length=30)  # Field name made lowercase.
    incent2per = models.SmallIntegerField(db_column='Incent2Per')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mst2Incent'


class Mstacc(models.Model):
    acckey = models.AutoField(db_column='AccKey', primary_key=True)  # Field name made lowercase.
    accname = models.CharField(db_column='AccName', max_length=40)  # Field name made lowercase.
    acccode = models.CharField(db_column='AccCode', unique=True, max_length=10)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=160)  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=20)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20)  # Field name made lowercase.
    keyperson = models.CharField(db_column='KeyPerson', max_length=30)  # Field name made lowercase.
    email = models.CharField(max_length=50)
    periodic = models.BooleanField(db_column='Periodic')  # Field name made lowercase.
    mstplkey = models.ForeignKey('Mstpl', models.DO_NOTHING, db_column='mstPLKey')  # Field name made lowercase.
    msg = models.CharField(db_column='Msg', max_length=200, blank=True, null=True)  # Field name made lowercase.
    defaultflag = models.BooleanField(db_column='DefaultFlag')  # Field name made lowercase.
    deductperc = models.SmallIntegerField(db_column='DeductPerc')  # Field name made lowercase.
    tallyledgac = models.CharField(db_column='TallyLedgAc', max_length=50)  # Field name made lowercase.
    isaccactive = models.BooleanField(db_column='IsAccActive')  # Field name made lowercase.
    iswebactive = models.BooleanField(db_column='IsWebActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstAcc'


class Mstaccrights(models.Model):
    oprkey = models.IntegerField(db_column='OPRKey', primary_key=True)  # Field name made lowercase.
    fillorder = models.SmallIntegerField(db_column='FillOrder')  # Field name made lowercase.
    formname = models.CharField(db_column='FormName', max_length=50)  # Field name made lowercase.
    objindex = models.SmallIntegerField(db_column='ObjIndex')  # Field name made lowercase.
    permitted = models.BooleanField(db_column='Permitted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstAccRights'
        unique_together = (('oprkey', 'fillorder', 'formname'),)


class Mstbarcode(models.Model):
    bcprinterid = models.CharField(db_column='BCPrinterID', primary_key=True, max_length=20)  # Field name made lowercase.
    prnformat = models.CharField(db_column='PRNFormat', max_length=5000)  # Field name made lowercase.
    defport = models.CharField(db_column='DefPort', max_length=50)  # Field name made lowercase.
    defflag = models.BooleanField(db_column='DefFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstBarCode'


class Mstbarcodepre(models.Model):
    bcprinterid = models.CharField(db_column='BCPrinterID', primary_key=True, max_length=20)  # Field name made lowercase.
    prnformat = models.CharField(db_column='PRNFormat', max_length=5000)  # Field name made lowercase.
    defport = models.CharField(db_column='DefPort', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstBarCodePre'


class Mstdept(models.Model):
    deptid = models.CharField(db_column='DeptID', primary_key=True, max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstDept'


class Mstdr(models.Model):
    mstdrkey = models.AutoField(db_column='mstDrKey', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=10)  # Field name made lowercase.
    drname = models.CharField(db_column='DrName', max_length=40)  # Field name made lowercase.
    drcode = models.CharField(db_column='DrCode', unique=True, max_length=10)  # Field name made lowercase.
    degree = models.CharField(db_column='Degree', max_length=30)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=20)  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=25)  # Field name made lowercase.
    pin = models.CharField(db_column='PIN', max_length=6)  # Field name made lowercase.
    phhosp = models.CharField(db_column='PhHosp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phresi = models.CharField(db_column='PhResi', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=15)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    married = models.DateTimeField(db_column='Married', blank=True, null=True)  # Field name made lowercase.
    spouse = models.CharField(db_column='Spouse', max_length=30)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=10)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=50)  # Field name made lowercase.
    dor = models.DateTimeField(db_column='DOR')  # Field name made lowercase.
    defaultflag = models.BooleanField(db_column='DefaultFlag')  # Field name made lowercase.
    mobile4sms = models.CharField(db_column='Mobile4SMS', max_length=39)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    visitrs = models.SmallIntegerField(db_column='VisitRs')  # Field name made lowercase.
    salesrep = models.CharField(db_column='SalesRep', max_length=50)  # Field name made lowercase.
    iswebactive = models.BooleanField(db_column='IsWebActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstDr'


class Mstdrincentrs(models.Model):
    mstitemkey = models.ForeignKey('Mstplitems', models.DO_NOTHING, db_column='mstItemKey', primary_key=True)  # Field name made lowercase.
    mstdrkey = models.ForeignKey(Mstdr, models.DO_NOTHING, db_column='mstDrKey')  # Field name made lowercase.
    incentivers = models.SmallIntegerField(db_column='IncentiveRs')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstDrIncentRs'
        unique_together = (('mstitemkey', 'mstdrkey'),)


class Mstdrincentive(models.Model):
    mstdrkey = models.ForeignKey(Mstdr, models.DO_NOTHING, db_column='mstDrKey', primary_key=True)  # Field name made lowercase.
    itemcatkey = models.ForeignKey('Mstitemcategory', models.DO_NOTHING, db_column='ItemCatKey')  # Field name made lowercase.
    incentive = models.SmallIntegerField(db_column='Incentive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstDrIncentive'
        unique_together = (('mstdrkey', 'itemcatkey'),)


class Msteqp(models.Model):
    eqppk = models.AutoField(db_column='EqpPK', primary_key=True)  # Field name made lowercase.
    eqpid = models.CharField(db_column='EqpID', unique=True, max_length=10)  # Field name made lowercase.
    eqpname = models.CharField(db_column='EqpName', max_length=30)  # Field name made lowercase.
    warrantydt = models.DateTimeField(db_column='WarrantyDt', blank=True, null=True)  # Field name made lowercase.
    purdt = models.DateTimeField(db_column='PurDt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstEqp'


class Mstexpcategory(models.Model):
    category = models.CharField(db_column='Category', primary_key=True, max_length=50)  # Field name made lowercase.
    tallyledgac = models.CharField(db_column='TallyLedgAc', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstExpCategory'


class Mstitemcategory(models.Model):
    itemcatkey = models.AutoField(db_column='ItemCatKey', primary_key=True)  # Field name made lowercase.
    itemcategory = models.CharField(db_column='ItemCategory', unique=True, max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstItemCategory'


class Mstitemrepotests(models.Model):
    mstitemkey = models.ForeignKey('Mstplitems', models.DO_NOTHING, db_column='mstItemKey', primary_key=True)  # Field name made lowercase.
    msttestkey = models.ForeignKey('Msttests', models.DO_NOTHING, db_column='mstTestKey')  # Field name made lowercase.
    mstrepokey = models.ForeignKey('Mstrepo', models.DO_NOTHING, db_column='mstRepoKey')  # Field name made lowercase.
    eorder = models.SmallIntegerField(db_column='EOrder')  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=150)  # Field name made lowercase.
    vrule = models.CharField(db_column='VRule', max_length=150)  # Field name made lowercase.
    vmsg = models.CharField(db_column='VMsg', max_length=20)  # Field name made lowercase.
    vrulemust = models.BooleanField(db_column='VRuleMust')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstItemRepoTests'
        unique_together = (('mstitemkey', 'msttestkey', 'mstrepokey'),)


class Mstmacros(models.Model):
    macropk = models.AutoField(db_column='MacroPk', primary_key=True)  # Field name made lowercase.
    repogrp = models.CharField(db_column='RepoGrp', max_length=20)  # Field name made lowercase.
    macrocode = models.CharField(db_column='MacroCode', max_length=20)  # Field name made lowercase.
    macrotext = models.TextField(db_column='MacroText')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mstMacros'
        unique_together = (('repogrp', 'macrocode'),)


class Mstnormals(models.Model):
    normalkey = models.AutoField(db_column='NormalKey', primary_key=True)  # Field name made lowercase.
    msttestkey = models.ForeignKey('Msttests', models.DO_NOTHING, db_column='mstTestKey')  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    normals = models.CharField(db_column='Normals', max_length=1000)  # Field name made lowercase.
    nlow = models.DecimalField(db_column='nLow', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nhigh = models.DecimalField(db_column='nHigh', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstNormals'
        unique_together = (('msttestkey', 'sex', 'age'),)


class Mstopr(models.Model):
    oprkey = models.AutoField(db_column='OPRKey', primary_key=True)  # Field name made lowercase.
    oprid = models.CharField(db_column='OPRID', unique=True, max_length=5)  # Field name made lowercase.
    oprname = models.CharField(db_column='OPRName', max_length=30)  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=10)  # Field name made lowercase.
    mobile4sms = models.CharField(db_column='Mobile4SMS', max_length=10)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    sngimg = models.BinaryField(db_column='SngImg', blank=True, null=True)  # Field name made lowercase.
    oprimgwidth = models.DecimalField(db_column='OprImgWidth', max_digits=10, decimal_places=4)  # Field name made lowercase.
    oprimgheight = models.DecimalField(db_column='OprImgHeight', max_digits=10, decimal_places=4)  # Field name made lowercase.
    oprimgleft = models.DecimalField(db_column='OprImgLeft', max_digits=10, decimal_places=4)  # Field name made lowercase.
    oprimgtop = models.DecimalField(db_column='OprImgTop', max_digits=10, decimal_places=4)  # Field name made lowercase.
    signloc = models.CharField(db_column='SignLoc', max_length=1)  # Field name made lowercase.
    auditlockdays = models.SmallIntegerField(db_column='AuditLockDays')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstOPR'


class Mstoprviewer(models.Model):
    oprid = models.CharField(db_column='OPRID', primary_key=True, max_length=20)  # Field name made lowercase.
    oprname = models.CharField(db_column='OPRName', max_length=50)  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=20)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    viewall = models.BooleanField(db_column='ViewAll')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstOPRViewer'


class Mstoptions(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    patientnamecase = models.CharField(db_column='PatientNameCase', max_length=1)  # Field name made lowercase.
    refdrnamecase = models.CharField(db_column='RefDrNameCase', max_length=1)  # Field name made lowercase.
    topmargin = models.DecimalField(db_column='TopMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    leftmargin = models.DecimalField(db_column='LeftMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    bottommargin = models.DecimalField(db_column='BottomMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    rightmargin = models.DecimalField(db_column='RightMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    deffont = models.CharField(db_column='DefFont', max_length=30)  # Field name made lowercase.
    deffontsize = models.SmallIntegerField(db_column='DefFontSize')  # Field name made lowercase.
    header = models.TextField(db_column='Header')  # Field name made lowercase. This field type is a guess.
    footer = models.TextField(db_column='Footer')  # Field name made lowercase. This field type is a guess.
    receipt = models.TextField(db_column='Receipt')  # Field name made lowercase. This field type is a guess.
    newlabno = models.SmallIntegerField(db_column='NewLabNo')  # Field name made lowercase.
    startmonth = models.SmallIntegerField(db_column='StartMonth')  # Field name made lowercase.
    uppbold = models.BooleanField(db_column='UppBold')  # Field name made lowercase.
    uppunderline = models.BooleanField(db_column='UppUnderLine')  # Field name made lowercase.
    uppitalic = models.BooleanField(db_column='UppItalic')  # Field name made lowercase.
    uppcolor = models.IntegerField(db_column='UppColor')  # Field name made lowercase.
    lowbold = models.BooleanField(db_column='LowBold')  # Field name made lowercase.
    lowunderline = models.BooleanField(db_column='LowUnderLine')  # Field name made lowercase.
    lowitalic = models.BooleanField(db_column='LowItalic')  # Field name made lowercase.
    lowcolor = models.IntegerField(db_column='LowColor')  # Field name made lowercase.
    uppfont = models.CharField(db_column='UppFont', max_length=50)  # Field name made lowercase.
    uppfsize = models.DecimalField(db_column='UppFSize', max_digits=10, decimal_places=4)  # Field name made lowercase.
    lowfont = models.CharField(db_column='LowFont', max_length=50)  # Field name made lowercase.
    lowfsize = models.DecimalField(db_column='LowFSize', max_digits=10, decimal_places=4)  # Field name made lowercase.
    labprefix = models.CharField(db_column='LabPrefix', max_length=5)  # Field name made lowercase.
    labsuffix = models.CharField(db_column='LabSuffix', max_length=2)  # Field name made lowercase.
    entryfrom = models.SmallIntegerField(db_column='EntryFrom')  # Field name made lowercase.
    labname = models.CharField(db_column='LabName', max_length=100)  # Field name made lowercase.
    labphone = models.CharField(db_column='LabPhone', max_length=50)  # Field name made lowercase.
    labaddr = models.CharField(db_column='LabAddr', max_length=300)  # Field name made lowercase.
    labdrname = models.CharField(db_column='LabDrName', max_length=50)  # Field name made lowercase.
    labplace = models.CharField(db_column='LabPlace', max_length=20)  # Field name made lowercase.
    addr4card = models.CharField(db_column='Addr4Card', max_length=300)  # Field name made lowercase.
    allowlabnoedit = models.BooleanField(db_column='AllowLabNoEdit')  # Field name made lowercase.
    cardfootnote = models.CharField(db_column='CardFootNote', max_length=60)  # Field name made lowercase.
    cellcounter = models.CharField(db_column='CellCounter', max_length=255)  # Field name made lowercase.
    defreporeadysms = models.CharField(db_column='DefRepoReadySMS', max_length=160)  # Field name made lowercase.
    stattopmarg = models.DecimalField(db_column='StatTopMarg', max_digits=10, decimal_places=4)  # Field name made lowercase.
    statbottmarg = models.DecimalField(db_column='StatBottMarg', max_digits=10, decimal_places=4)  # Field name made lowercase.
    allowage = models.BooleanField(db_column='AllowAge')  # Field name made lowercase.
    allowsex = models.BooleanField(db_column='AllowSex')  # Field name made lowercase.
    graphlayout = models.CharField(db_column='GraphLayout', max_length=1)  # Field name made lowercase.
    graphimgpath = models.CharField(db_column='GraphImgPath', max_length=100)  # Field name made lowercase.
    jobcardno = models.SmallIntegerField(db_column='JobCardNo')  # Field name made lowercase.
    auditlockdt = models.DateTimeField(db_column='AuditLockDt')  # Field name made lowercase.
    billtopmargin = models.DecimalField(db_column='BillTopMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    billleftmargin = models.DecimalField(db_column='BillLeftMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    printbillheader = models.BooleanField(db_column='PrintBillHeader')  # Field name made lowercase.
    recptopmargin = models.DecimalField(db_column='RecpTopMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    recpleftmargin = models.DecimalField(db_column='RecpLeftMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    printrecpheader = models.BooleanField(db_column='PrintRecpHeader')  # Field name made lowercase.
    drfindbycode = models.BooleanField(db_column='DrFindByCode')  # Field name made lowercase.
    invfindbycode = models.BooleanField(db_column='InvFindByCode')  # Field name made lowercase.
    useprefix = models.BooleanField(db_column='UsePrefix')  # Field name made lowercase.
    usesuffix = models.BooleanField(db_column='UseSuffix')  # Field name made lowercase.
    usememberid = models.BooleanField(db_column='UseMemberID')  # Field name made lowercase.
    usephone = models.BooleanField(db_column='UsePhone')  # Field name made lowercase.
    usesendby = models.BooleanField(db_column='UseSendBy')  # Field name made lowercase.
    useaddress = models.BooleanField(db_column='UseAddress')  # Field name made lowercase.
    useplace = models.BooleanField(db_column='UsePlace')  # Field name made lowercase.
    userefid = models.BooleanField(db_column='UseRefID')  # Field name made lowercase.
    userefdr2 = models.BooleanField(db_column='UseRefDr2')  # Field name made lowercase.
    usemobile4sms = models.BooleanField(db_column='UseMobile4SMS')  # Field name made lowercase.
    useemailid = models.BooleanField(db_column='UseEmailID')  # Field name made lowercase.
    usenotes = models.BooleanField(db_column='UseNotes')  # Field name made lowercase.
    prnrefnoinbill = models.BooleanField(db_column='PrnRefNoInBill')  # Field name made lowercase.
    prnrefnoinrecp = models.BooleanField(db_column='PrnRefNoInRecp')  # Field name made lowercase.
    cardtopmargin = models.DecimalField(db_column='CardTopMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    cardleftmargin = models.DecimalField(db_column='CardLeftMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    labnocont = models.BooleanField(db_column='LabNoCont')  # Field name made lowercase.
    consent = models.TextField(db_column='Consent')  # Field name made lowercase. This field type is a guess.
    billorient = models.SmallIntegerField(db_column='BillOrient')  # Field name made lowercase.
    recporient = models.SmallIntegerField(db_column='RecpOrient')  # Field name made lowercase.
    jobcardudtop = models.DecimalField(db_column='JobCardUdTop', max_digits=10, decimal_places=4)  # Field name made lowercase.
    jobcardudleft = models.DecimalField(db_column='JobCardUdLeft', max_digits=10, decimal_places=4)  # Field name made lowercase.
    userdefcard = models.TextField(db_column='UserdefCard')  # Field name made lowercase. This field type is a guess.
    num_auto = models.BooleanField(db_column='num_Auto')  # Field name made lowercase.
    num_reset = models.SmallIntegerField(db_column='num_Reset')  # Field name made lowercase.
    ref_dup = models.BooleanField(db_column='Ref_Dup')  # Field name made lowercase.
    userefdraddbut = models.BooleanField(db_column='UseRefDrAddBut')  # Field name made lowercase.
    usepattitle = models.BooleanField(db_column='UsePatTitle')  # Field name made lowercase.
    preoprsign = models.BooleanField(db_column='PreOprSign')  # Field name made lowercase.
    pw4viewall = models.CharField(db_column='PW4ViewAll', max_length=20)  # Field name made lowercase.
    sendername4sms = models.CharField(db_column='SenderName4SMS', max_length=30)  # Field name made lowercase.
    preiodicbillnotes = models.TextField(db_column='PreiodicBillNotes')  # Field name made lowercase. This field type is a guess.
    smtpserver = models.CharField(db_column='SMTPServer', max_length=50)  # Field name made lowercase.
    smtpport = models.CharField(db_column='SMTPPort', max_length=4)  # Field name made lowercase.
    smtpreqssl = models.BooleanField(db_column='SMTPReqSSL')  # Field name made lowercase.
    smtpaccname = models.CharField(db_column='SMTPAccName', max_length=50)  # Field name made lowercase.
    smtpaccpw = models.CharField(db_column='SMTPAccPW', max_length=50)  # Field name made lowercase.
    smtpfromname = models.CharField(db_column='SMTPFromName', max_length=50)  # Field name made lowercase.
    smtpfromemail = models.CharField(db_column='SMTPFromEmail', max_length=50)  # Field name made lowercase.
    uniquesampno = models.BooleanField(db_column='UniqueSampNo')  # Field name made lowercase.
    cashbillext = models.BooleanField(db_column='CashBillExt')  # Field name made lowercase.
    cashreceiptext = models.BooleanField(db_column='CashReceiptExt')  # Field name made lowercase.
    periodicbillext = models.BooleanField(db_column='PeriodicBillExt')  # Field name made lowercase.
    periodicreceiptext = models.BooleanField(db_column='PeriodicReceiptExt')  # Field name made lowercase.
    periodicbilldetext = models.BooleanField(db_column='PeriodicBillDetExt')  # Field name made lowercase.
    jobcardext = models.BooleanField(db_column='JobCardExt')  # Field name made lowercase.
    reqslipext = models.BooleanField(db_column='ReqSlipExt')  # Field name made lowercase.
    expensevchext = models.BooleanField(db_column='ExpenseVchExt')  # Field name made lowercase.
    purchaseext = models.BooleanField(db_column='PurchaseExt')  # Field name made lowercase.
    stkissueext = models.BooleanField(db_column='StkIssueExt')  # Field name made lowercase.
    autosms = models.CharField(db_column='AutoSMS', max_length=320)  # Field name made lowercase.
    duecheck = models.BooleanField(db_column='DueCheck')  # Field name made lowercase.
    phone2mob4sms = models.BooleanField(db_column='Phone2Mob4SMS')  # Field name made lowercase.
    brid4webrepo = models.CharField(db_column='BrID4WebRepo', max_length=1)  # Field name made lowercase.
    localfilepath = models.CharField(db_column='LocalFilePath', max_length=255)  # Field name made lowercase.
    smsdelimchar = models.CharField(db_column='SMSDelimChar', max_length=5, blank=True, null=True)  # Field name made lowercase.
    defsamplestatus = models.SmallIntegerField(db_column='DefSampleStatus', blank=True, null=True)  # Field name made lowercase.
    autoemailrefdr = models.BooleanField(db_column='AutoEmailRefDr', blank=True, null=True)  # Field name made lowercase.
    autoemailpat = models.BooleanField(db_column='AutoEmailPat', blank=True, null=True)  # Field name made lowercase.
    autoemailacc = models.BooleanField(db_column='AutoEmailAcc', blank=True, null=True)  # Field name made lowercase.
    autowebupload = models.BooleanField(db_column='AutoWebUpload', blank=True, null=True)  # Field name made lowercase.
    lastprebarcodeno = models.CharField(db_column='LastPreBarCodeNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lastautoprebarcodeno = models.BigIntegerField(db_column='LastAutoPreBarCodeNo', blank=True, null=True)  # Field name made lowercase.
    autoprebarcodenoprefix = models.CharField(db_column='AutoPreBarCodeNoPrefix', max_length=3, blank=True, null=True)  # Field name made lowercase.
    displaybackupmsg = models.BooleanField(db_column='DisplayBackupMsg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstOptions'


class Mstpl(models.Model):
    mstplkey = models.AutoField(db_column='mstPLKey', primary_key=True)  # Field name made lowercase.
    plname = models.CharField(db_column='PLName', max_length=30)  # Field name made lowercase.
    pldesc = models.CharField(db_column='PLDesc', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstPL'


class Mstplitems(models.Model):
    mstitemkey = models.AutoField(db_column='mstItemKey', primary_key=True)  # Field name made lowercase.
    mstplkey = models.ForeignKey(Mstpl, models.DO_NOTHING, db_column='mstPLKey')  # Field name made lowercase.
    item = models.CharField(db_column='Item', max_length=60)  # Field name made lowercase.
    rate = models.SmallIntegerField(db_column='Rate')  # Field name made lowercase.
    collection = models.CharField(db_column='Collection', max_length=120)  # Field name made lowercase.
    printinrecp = models.BooleanField(db_column='PrintInRecp')  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=10)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    category = models.ForeignKey(Mstitemcategory, models.DO_NOTHING, db_column='Category')  # Field name made lowercase.
    outsourced = models.BooleanField(db_column='Outsourced')  # Field name made lowercase.
    repofreq = models.CharField(db_column='RepoFreq', max_length=80)  # Field name made lowercase.
    repocolltime = models.CharField(db_column='RepoCollTime', max_length=80)  # Field name made lowercase.
    outsrcto = models.CharField(db_column='OutSrcTo', max_length=50)  # Field name made lowercase.
    tubecolors = models.CharField(db_column='TubeColors', max_length=70)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstPLItems'
        unique_together = (('mstplkey', 'shortname'),)


class Mstpresuf(models.Model):
    presufpk = models.AutoField(db_column='PreSufPk', primary_key=True)  # Field name made lowercase.
    presuftext = models.CharField(db_column='PreSufText', max_length=5)  # Field name made lowercase.
    presuf = models.CharField(db_column='PreSuf', max_length=1)  # Field name made lowercase.
    defflag = models.BooleanField(db_column='DefFlag')  # Field name made lowercase.
    header = models.TextField(db_column='Header')  # Field name made lowercase. This field type is a guess.
    footer = models.TextField(db_column='Footer')  # Field name made lowercase. This field type is a guess.
    topmargin = models.DecimalField(db_column='TopMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    leftmargin = models.DecimalField(db_column='LeftMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    bottommargin = models.DecimalField(db_column='BottomMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    rightmargin = models.DecimalField(db_column='RightMargin', max_digits=10, decimal_places=4)  # Field name made lowercase.
    headimg = models.CharField(db_column='HeadImg', max_length=500)  # Field name made lowercase.
    signimg = models.CharField(db_column='SignImg', max_length=500)  # Field name made lowercase.
    prnsignemail = models.BooleanField(db_column='PrnSignEmail')  # Field name made lowercase.
    prnsignrepo = models.BooleanField(db_column='PrnSignRepo')  # Field name made lowercase.
    prnheademail = models.BooleanField(db_column='PrnHeadEmail')  # Field name made lowercase.
    prnheadrepo = models.BooleanField(db_column='PrnHeadRepo')  # Field name made lowercase.
    headerimg = models.BinaryField(db_column='HeaderImg', blank=True, null=True)  # Field name made lowercase.
    sngimg = models.BinaryField(db_column='SngImg', blank=True, null=True)  # Field name made lowercase.
    remotenodename = models.CharField(db_column='RemoteNodeName', max_length=70)  # Field name made lowercase.
    preimgwidth = models.DecimalField(db_column='PreImgWidth', max_digits=10, decimal_places=4)  # Field name made lowercase.
    preimgheight = models.DecimalField(db_column='PreImgHeight', max_digits=10, decimal_places=4)  # Field name made lowercase.
    preimgleft = models.DecimalField(db_column='PreImgLeft', max_digits=10, decimal_places=4)  # Field name made lowercase.
    preimgtop = models.DecimalField(db_column='PreImgTop', max_digits=10, decimal_places=4)  # Field name made lowercase.
    signloc = models.CharField(db_column='SignLoc', max_length=1)  # Field name made lowercase.
    acckey = models.IntegerField(db_column='AccKey')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstPreSuf'
        unique_together = (('presuftext', 'presuf'),)


class Mstrs232(models.Model):
    instno = models.SmallIntegerField(db_column='InstNo', primary_key=True)  # Field name made lowercase.
    instid = models.CharField(db_column='InstID', max_length=1)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=10)  # Field name made lowercase.
    instname = models.CharField(db_column='InstName', max_length=50)  # Field name made lowercase.
    cellcounter = models.BooleanField(db_column='CellCounter')  # Field name made lowercase.
    deldatadays = models.SmallIntegerField(db_column='DelDataDays')  # Field name made lowercase.
    graphimgpath = models.CharField(db_column='GraphImgPath', max_length=500)  # Field name made lowercase.
    parameters = models.CharField(db_column='Parameters', max_length=1000)  # Field name made lowercase.
    autoverify = models.BooleanField(db_column='AutoVerify')  # Field name made lowercase.
    printgraphs = models.BooleanField(db_column='PrintGraphs')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstRS232'


class Mstrs232Formula(models.Model):
    instno = models.ForeignKey(Mstrs232, models.DO_NOTHING, db_column='InstNo', primary_key=True)  # Field name made lowercase.
    insttestid = models.CharField(db_column='InstTestID', max_length=20)  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstRS232Formula'
        unique_together = (('instno', 'insttestid'),)


class Mstrs232Tests(models.Model):
    mst232Testpk = models.AutoField(db_column='PK', primary_key=True)  # Field name made lowercase.
    instno = models.ForeignKey(Mstrs232, models.DO_NOTHING, db_column='InstNo')  # Field name made lowercase.
    listestid = models.CharField(db_column='LISTestID', max_length=10)  # Field name made lowercase.
    insttestid = models.CharField(db_column='InstTestID', max_length=20)  # Field name made lowercase.
    altinsttestid = models.CharField(db_column='AltInstTestID', max_length=20)  # Field name made lowercase.
    sampletype = models.CharField(db_column='SampleType', max_length=20)  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstRS232Tests'
        unique_together = (('instno', 'listestid', 'insttestid', 'suffix'),)


class Mstrepo(models.Model):
    mstrepokey = models.AutoField(db_column='mstRepoKey', primary_key=True)  # Field name made lowercase.
    repoid = models.CharField(db_column='RepoID', unique=True, max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    rtfdata = models.TextField(db_column='RTFData')  # Field name made lowercase. This field type is a guess.
    repogrpkey = models.ForeignKey('Mstrepogrp', models.DO_NOTHING, db_column='RepoGrpKey')  # Field name made lowercase.
    printhisto = models.BooleanField(db_column='PrintHisto')  # Field name made lowercase.
    includeheader = models.BooleanField(db_column='IncludeHeader')  # Field name made lowercase.
    includefooter = models.BooleanField(db_column='IncludeFooter')  # Field name made lowercase.
    tatinmm = models.SmallIntegerField(db_column='TATinMM')  # Field name made lowercase.
    samplename = models.CharField(db_column='SampleName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    autoverify = models.BooleanField(db_column='AutoVerify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstRepo'


class Mstrepogrp(models.Model):
    repogrpkey = models.AutoField(db_column='RepoGrpKey', primary_key=True)  # Field name made lowercase.
    repogrp = models.CharField(db_column='RepoGrp', unique=True, max_length=20)  # Field name made lowercase.
    prefix = models.CharField(db_column='Prefix', max_length=3)  # Field name made lowercase.
    lastno = models.IntegerField(db_column='LastNo')  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=2)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstRepoGrp'


class Mstrepotests(models.Model):
    mstrepotestkey = models.AutoField(db_column='mstRepoTestKey', primary_key=True)  # Field name made lowercase.
    mstrepokey = models.ForeignKey(Mstrepo, models.DO_NOTHING, db_column='mstRepoKey')  # Field name made lowercase.
    msttestkey = models.ForeignKey('Msttests', models.DO_NOTHING, db_column='mstTestKey')  # Field name made lowercase.
    eorder = models.SmallIntegerField(db_column='EOrder')  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=150)  # Field name made lowercase.
    vrule = models.CharField(db_column='VRule', max_length=150)  # Field name made lowercase.
    vmsg = models.CharField(db_column='VMsg', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstRepoTests'
        unique_together = (('mstrepokey', 'msttestkey'),)


class Mstsmschrreplace(models.Model):
    #Mstsmschrreplacepk = models.AutoField(db_column='PK', primary_key=True, )  # Field name made lowercase.
    smschar2replace = models.CharField(db_column='SMSChar2Replace', primary_key=True, max_length=1)  # Field name made lowercase.
    smsreplacewith = models.CharField(db_column='SMSReplaceWith', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstSMSChrReplace'


class Mstsmstp(models.Model):
    smstpid = models.CharField(db_column='SMSTPID', primary_key=True, max_length=10)  # Field name made lowercase.
    smstpname = models.CharField(db_column='SMSTPName', max_length=100)  # Field name made lowercase.
    smstp = models.CharField(db_column='SMSTP', max_length=2000)  # Field name made lowercase.
    smsrepeattp = models.CharField(db_column='SMSRepeatTP', max_length=500)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstSMSTP'


class Mstsamplefrom(models.Model):
    mstsfkey = models.AutoField(db_column='mstSFKey', primary_key=True)  # Field name made lowercase.
    samplefrom = models.CharField(db_column='SampleFrom', max_length=40)  # Field name made lowercase.
    sfid = models.CharField(db_column='SFID', unique=True, max_length=10)  # Field name made lowercase.
    defaultflag = models.BooleanField(db_column='DefaultFlag')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20)  # Field name made lowercase.
    issfactive = models.BooleanField(db_column='IsSFActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstSampleFrom'


class Mstsamplenames(models.Model):
    mstsamplepk = models.AutoField(db_column='mstSamplePK', primary_key=True)  # Field name made lowercase.
    samplename = models.CharField(db_column='SampleName', unique=True, max_length=120)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstSampleNames'


class Mstsamplesuffix(models.Model):
    mstsamplesuffixpk = models.AutoField(db_column='mstSampleSuffixPK', primary_key=True)  # Field name made lowercase.
    samplesuffix = models.CharField(db_column='SampleSuffix', unique=True, max_length=5)  # Field name made lowercase.
    samplesuffixname = models.CharField(db_column='SampleSuffixName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstSampleSuffix'


class Mstsecctrl(models.Model):
    p0 = models.CharField(db_column='P0', max_length=3000)  # Field name made lowercase.
    p1 = models.CharField(db_column='P1', max_length=3000)  # Field name made lowercase.
    p2 = models.CharField(db_column='P2', max_length=3000)  # Field name made lowercase.
    p3 = models.CharField(db_column='P3', max_length=3000)  # Field name made lowercase.
    p4 = models.CharField(db_column='P4', max_length=3000)  # Field name made lowercase.
    p5 = models.CharField(db_column='P5', max_length=3000)  # Field name made lowercase.
    p6 = models.CharField(db_column='P6', max_length=3000)  # Field name made lowercase.
    p7 = models.CharField(db_column='P7', max_length=3000)  # Field name made lowercase.
    p8 = models.CharField(db_column='P8', max_length=3000)  # Field name made lowercase.
    p9 = models.CharField(db_column='P9', max_length=3000)  # Field name made lowercase.
    p10 = models.CharField(db_column='P10', max_length=3000)  # Field name made lowercase.
    p11 = models.CharField(db_column='P11', max_length=3000)  # Field name made lowercase.
    p12 = models.CharField(db_column='P12', max_length=3000)  # Field name made lowercase.
    mstsecctrlpk = models.SmallIntegerField(db_column='PK', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstSecCtrl'


class Mstspecialpsw(models.Model):
    specialparam = models.CharField(db_column='SpecialParam', primary_key=True, max_length=15)  # Field name made lowercase.
    specialpsw = models.CharField(db_column='SpecialPsw', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstSpecialPsw'


class Mststock(models.Model):
    mstitemkey = models.AutoField(db_column='mstItemKey', primary_key=True)  # Field name made lowercase.
    itemid = models.CharField(db_column='ItemID', unique=True, max_length=10)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=30)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=10, decimal_places=4)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=10)  # Field name made lowercase.
    issuerate = models.DecimalField(db_column='IssueRate', max_digits=10, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstStock'


class Msttally(models.Model):
    cashsalesac = models.CharField(db_column='CashSalesAc', max_length=50)  # Field name made lowercase.
    periodicsalesac = models.CharField(db_column='PeriodicSalesAc', max_length=50)  # Field name made lowercase.
    bankac = models.CharField(db_column='BankAc', max_length=50)  # Field name made lowercase.
    cashac = models.CharField(db_column='CashAc', max_length=50)  # Field name made lowercase.
    tdsac = models.CharField(db_column='TDSAc', max_length=50)  # Field name made lowercase.
    tallyip = models.CharField(db_column='TallyIP', max_length=20)  # Field name made lowercase.
    tallyport = models.SmallIntegerField(db_column='TallyPort')  # Field name made lowercase.
    tallyuser = models.CharField(db_column='TallyUser', max_length=30)  # Field name made lowercase.
    tallypass = models.CharField(db_column='TallyPass', max_length=30)  # Field name made lowercase.
    compname = models.CharField(db_column='CompName', max_length=50)  # Field name made lowercase.
    compguid = models.CharField(db_column='CompGUID', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstTally'


class Msttests(models.Model):
    msttestkey = models.AutoField(db_column='mstTestKey', primary_key=True)  # Field name made lowercase.
    test = models.CharField(db_column='Test', max_length=100)  # Field name made lowercase.
    testid = models.CharField(db_column='TestID', unique=True, max_length=10)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=180)  # Field name made lowercase.
    options = models.CharField(db_column='Options', max_length=5000)  # Field name made lowercase.
    analyzer = models.CharField(db_column='Analyzer', max_length=10)  # Field name made lowercase.
    anatest = models.CharField(db_column='AnaTest', max_length=10)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    dept = models.ForeignKey(Mstdept, models.DO_NOTHING, db_column='Dept')  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=10, blank=True, null=True)  # Field name made lowercase.
    printincard = models.BooleanField(db_column='PrintInCard')  # Field name made lowercase.
    normals = models.CharField(db_column='Normals', max_length=100)  # Field name made lowercase.
    test4sms = models.CharField(db_column='Test4SMS', max_length=50)  # Field name made lowercase.
    visible2all = models.BooleanField(db_column='Visible2All')  # Field name made lowercase.
    tatinmm = models.SmallIntegerField(db_column='TATinMM')  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=200, blank=True, null=True)  # Field name made lowercase.
    vrule = models.CharField(db_column='VRule', max_length=200, blank=True, null=True)  # Field name made lowercase.
    vmsg = models.CharField(db_column='VMsg', max_length=30, blank=True, null=True)  # Validation Message.
    vrulemust = models.BooleanField(db_column='VRuleMust', blank=True, null=True)  # Validation if must ?.

    class Meta:
        managed = False
        db_table = 'mstTests'


class Msttestscalc(models.Model):
    mstrepokey = models.ForeignKey(Mstrepo, models.DO_NOTHING, db_column='mstRepoKey', primary_key=True)  # Field name made lowercase.
    condorder = models.SmallIntegerField(db_column='CondOrder')  # Field name made lowercase.
    ifcond = models.CharField(db_column='IfCond', max_length=5000)  # Field name made lowercase.
    trueval = models.CharField(db_column='TrueVal', max_length=180)  # Field name made lowercase.
    falseval = models.CharField(db_column='FalseVal', max_length=180)  # Field name made lowercase.
    calctestid = models.CharField(db_column='CalcTestID', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstTestsCalc'
        unique_together = (('mstrepokey', 'condorder'),)


class Mstwebupload(models.Model):
    domainname = models.CharField(db_column='DomainName', max_length=100)  # Field name made lowercase.
    domainfilepath = models.CharField(db_column='DomainFilePath', max_length=100)  # Field name made lowercase.
    localfilepath = models.CharField(db_column='LocalFilePath', max_length=100)  # Field name made lowercase.
    ftphost = models.CharField(db_column='FTPHost', max_length=100)  # Field name made lowercase.
    ftpuserid = models.CharField(db_column='FTPUserID', max_length=100)  # Field name made lowercase.
    ftppassword = models.CharField(db_column='FTPPassword', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstWebUpload'


class Tblaccdepo(models.Model):
    depopk = models.AutoField(db_column='DepoPK', primary_key=True)  # Field name made lowercase.
    acckey = models.ForeignKey(Mstacc, models.DO_NOTHING, db_column='AccKey')  # Field name made lowercase.
    depodate = models.DateTimeField(db_column='DepoDate')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAccDepo'


class Tblbills(models.Model):
    billkey = models.AutoField(db_column='BillKey', primary_key=True)  # Field name made lowercase.
    acckey = models.ForeignKey(Mstacc, models.DO_NOTHING, db_column='AccKey')  # Field name made lowercase.
    billno = models.SmallIntegerField(db_column='BillNo')  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate')  # Field name made lowercase.
    billfrom = models.DateTimeField(db_column='BillFrom')  # Field name made lowercase.
    billto = models.DateTimeField(db_column='BillTo')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount')  # Field name made lowercase.
    oprkey = models.IntegerField(db_column='OPRKey')  # Field name made lowercase.
    printed = models.BooleanField(db_column='Printed')  # Field name made lowercase.
    particular = models.CharField(db_column='Particular', max_length=1000)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=60)  # Field name made lowercase.
    postdate = models.DateTimeField(db_column='PostDate', blank=True, null=True)  # Field name made lowercase.
    postby = models.IntegerField(db_column='PostBy', blank=True, null=True)  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBills'


class Tblblocks(models.Model):
    blockkey = models.AutoField(db_column='BlockKey', primary_key=True)  # Field name made lowercase.
    repokey = models.ForeignKey('Tblrepo', models.DO_NOTHING, db_column='RepoKey')  # Field name made lowercase.
    blockno = models.IntegerField(db_column='BlockNo')  # Field name made lowercase.
    blockyear = models.SmallIntegerField(db_column='BlockYear')  # Field name made lowercase.
    blocknoyear = models.CharField(db_column='BlockNoYear', max_length=9, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBlocks'
        unique_together = (('blockyear', 'blockno'),)


class Tblcptitem(models.Model):
    itemkey = models.ForeignKey('Tblcostpertest', models.DO_NOTHING, db_column='ItemKey', primary_key=True)  # Field name made lowercase.
    testid = models.CharField(db_column='TestID', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCPTItem'
        unique_together = (('itemkey', 'testid'),)


class Tblcontacts(models.Model):
    mstffkey = models.AutoField(db_column='mstFFKey', primary_key=True)  # Field name made lowercase.
    ffname = models.CharField(db_column='FFName', max_length=40)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=60)  # Field name made lowercase.
    addr = models.CharField(db_column='Addr', max_length=255)  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=20)  # Field name made lowercase.
    pin = models.CharField(db_column='PIN', max_length=6)  # Field name made lowercase.
    phoff = models.CharField(db_column='PhOff', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phresi = models.CharField(db_column='PhResi', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    married = models.DateTimeField(db_column='Married', blank=True, null=True)  # Field name made lowercase.
    spouse = models.CharField(db_column='Spouse', max_length=30)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=10)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=50)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblContacts'


class Tblcostpertest(models.Model):
    tblitemkey = models.AutoField(db_column='tblItemKey', primary_key=True)  # Field name made lowercase.
    item = models.CharField(db_column='Item', max_length=30)  # Field name made lowercase.
    fdate = models.DateTimeField(db_column='FDate')  # Field name made lowercase.
    tdate = models.DateTimeField(db_column='TDate', blank=True, null=True)  # Field name made lowercase.
    cost = models.SmallIntegerField(db_column='Cost')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCostPerTest'


class Tblemail(models.Model):
    emailpk = models.AutoField(db_column='EmailPK', primary_key=True)  # Field name made lowercase.
    emaillabkey = models.IntegerField(db_column='EmailLabKey')  # Field name made lowercase.
    emailrepokey = models.IntegerField(db_column='EmailRepoKey')  # Field name made lowercase.
    emailrepoid = models.CharField(db_column='EmailRepoID', max_length=10)  # Field name made lowercase.
    emailorderdate = models.DateTimeField(db_column='EmailOrderDate')  # Field name made lowercase.
    emailstatusflag = models.CharField(db_column='EmailStatusFlag', max_length=1)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=254)  # Field name made lowercase.
    emailto = models.CharField(db_column='EmailTo', max_length=1)  # Field name made lowercase.
    emailfile = models.CharField(db_column='EmailFile', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblEmail'


class Tbleqpmaint(models.Model):
    eqpmaintpk = models.AutoField(db_column='EqpMaintPK', primary_key=True)  # Field name made lowercase.
    eqppk = models.ForeignKey(Msteqp, models.DO_NOTHING, db_column='EqpPK')  # Field name made lowercase.
    eqpschpk = models.ForeignKey('Tbleqpsch', models.DO_NOTHING, db_column='EqpSchPK', blank=True, null=True)  # Field name made lowercase.
    maintdt = models.DateTimeField(db_column='MaintDt')  # Field name made lowercase.
    maintrs = models.IntegerField(db_column='MaintRs')  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblEqpMaint'


class Tbleqpsch(models.Model):
    eqpschpk = models.AutoField(db_column='EqpSchPK', primary_key=True)  # Field name made lowercase.
    eqppk = models.ForeignKey(Msteqp, models.DO_NOTHING, db_column='EqpPK')  # Field name made lowercase.
    schdt = models.DateTimeField(db_column='SchDt')  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblEqpSch'


class Tblexpense(models.Model):
    expkey = models.AutoField(db_column='ExpKey', primary_key=True)  # Field name made lowercase.
    expdate = models.DateTimeField(db_column='ExpDate')  # Field name made lowercase.
    particulars = models.CharField(db_column='Particulars', max_length=250)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    oprid = models.CharField(db_column='OprID', max_length=5)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=50)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=30)  # Field name made lowercase.
    vchno = models.IntegerField(db_column='VchNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExpense'


class Tblhistoimgpath(models.Model):
    imgkey = models.BigAutoField(db_column='ImgKey', primary_key=True)  # Field name made lowercase.
    labno = models.CharField(db_column='LabNo', max_length=20)  # Field name made lowercase.
    testdate = models.DateTimeField(db_column='TestDate')  # Field name made lowercase.
    imgpath = models.CharField(db_column='ImgPath', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblHistoImgPath'


class Tblimg(models.Model):
    repokey = models.ForeignKey('Tblrepo', models.DO_NOTHING, db_column='RepoKey', primary_key=True)  # Field name made lowercase.
    img1 = models.BinaryField(db_column='Img1', blank=True, null=True)  # Field name made lowercase.
    img1notes = models.CharField(db_column='Img1Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    img2 = models.BinaryField(db_column='Img2', blank=True, null=True)  # Field name made lowercase.
    img2notes = models.CharField(db_column='Img2Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    img3 = models.BinaryField(db_column='Img3', blank=True, null=True)  # Field name made lowercase.
    img3notes = models.CharField(db_column='Img3Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    img4 = models.BinaryField(db_column='Img4', blank=True, null=True)  # Field name made lowercase.
    img4notes = models.CharField(db_column='Img4Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    img5 = models.BinaryField(db_column='Img5', blank=True, null=True)  # Field name made lowercase.
    img5notes = models.CharField(db_column='Img5Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    img6 = models.BinaryField(db_column='Img6', blank=True, null=True)  # Field name made lowercase.
    img6notes = models.CharField(db_column='Img6Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblImg'


class Tblimgpath(models.Model):
    imgpathpk = models.AutoField(db_column='imgPathPK', primary_key=True)  # Field name made lowercase.
    repokey = models.ForeignKey('Tblrepo', models.DO_NOTHING, db_column='RepoKey')  # Field name made lowercase.
    imgpath = models.CharField(db_column='imgPath', max_length=255)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblImgPath'


class Tblinv(models.Model):
    invkey = models.AutoField(db_column='InvKey', primary_key=True)  # Field name made lowercase.
    labkey = models.ForeignKey('Tbllab', models.DO_NOTHING, db_column='LabKey')  # Field name made lowercase.
    item = models.CharField(db_column='Item', max_length=60)  # Field name made lowercase.
    rate = models.SmallIntegerField(db_column='Rate')  # Field name made lowercase.
    printinrecp = models.BooleanField(db_column='PrintInRecp')  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=10)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=5)  # Field name made lowercase.
    incentive = models.SmallIntegerField(db_column='Incentive')  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=15)  # Field name made lowercase.
    outsourced = models.BooleanField(db_column='Outsourced')  # Field name made lowercase.
    repofreq = models.CharField(db_column='RepoFreq', max_length=80)  # Field name made lowercase.
    repocolltime = models.CharField(db_column='RepoCollTime', max_length=80)  # Field name made lowercase.
    incentivers = models.SmallIntegerField(db_column='IncentiveRs')  # Field name made lowercase.
    outsrcto = models.CharField(db_column='OutSrcTo', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInv'


class Tbllab(models.Model):
    labkey = models.AutoField(db_column='LabKey', primary_key=True)  # Field name made lowercase.
    dor = models.DateTimeField(db_column='DOR')  # Field name made lowercase.
    prefix = models.CharField(db_column='Prefix', max_length=5)  # Field name made lowercase.
    labno = models.IntegerField(db_column='LabNo')  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=2)  # Field name made lowercase.
    patid = models.CharField(db_column='PatID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=20)  # Field name made lowercase.
    mname = models.CharField(db_column='MName', max_length=20)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=20)  # Field name made lowercase.
    #patname is disabled as it donot allow to run views.discount=>e.save() line to execute as this field is compund field
    #patname = models.CharField(db_column='PatName', max_length=62)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1)  # Field name made lowercase.
    age = models.DecimalField(db_column='Age', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ageunit = models.CharField(db_column='AgeUnit', max_length=6)  # Field name made lowercase.
    acckey = models.ForeignKey(Mstacc, models.DO_NOTHING, db_column='AccKey')  # Field name made lowercase.
    plkey = models.IntegerField(db_column='PLKey')  # Field name made lowercase.
    sfkey = models.ForeignKey(Mstsamplefrom, models.DO_NOTHING, db_column='SFKey')  # Field name made lowercase.
    addr = models.CharField(db_column='Addr', max_length=120)  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=20)  # Field name made lowercase.
    sendby = models.CharField(db_column='SendBy', max_length=10)  # Field name made lowercase.
    urgent = models.BooleanField(db_column='Urgent')  # Field name made lowercase.
    disc = models.SmallIntegerField(db_column='Disc')  # Field name made lowercase.
    discby = models.IntegerField(db_column='DiscBy', blank=True, null=True)  # Field name made lowercase.
    discnote = models.CharField(db_column='DiscNote', max_length=50)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=50)  # Field name made lowercase.
    opr = models.ForeignKey(Mstopr, models.DO_NOTHING, db_column='OPR')  # Field name made lowercase.
    refid = models.CharField(db_column='RefID', max_length=25)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15)  # Field name made lowercase.
    refdr = models.ForeignKey(Mstdr, models.DO_NOTHING, db_column='RefDr')  # Field name made lowercase.
    refdr2 = models.CharField(db_column='RefDr2', max_length=60)  # Field name made lowercase.
    foc = models.BooleanField(db_column='FOC')  # Field name made lowercase.
    periodic = models.BooleanField(db_column='Periodic')  # Field name made lowercase.
    comm = models.SmallIntegerField(db_column='Comm')  # Field name made lowercase.
    mobile4sms = models.CharField(db_column='Mobile4SMS', max_length=12)  # Field name made lowercase.
    smsresults = models.BooleanField(db_column='SMSResults')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80)  # Field name made lowercase.
    deductamt = models.IntegerField(db_column='DeductAmt')  # Field name made lowercase.
    companion = models.CharField(db_column='Companion', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rel2pat = models.CharField(db_column='Rel2Pat', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billno = models.IntegerField(db_column='BillNo')  # Field name made lowercase.
    billprinted = models.SmallIntegerField(db_column='BillPrinted')  # Field name made lowercase.
    sampno = models.SmallIntegerField(db_column='SampNo')  # Field name made lowercase.
    #labrefno is disabled as it donot allow to run views.discount=>e.save() line to execute as this field is compund field
    #labrefno = models.CharField(db_column='LabRefNo', max_length=17, blank=True, null=True)  # Field name made lowercase.
    incent2name = models.CharField(db_column='Incent2Name', max_length=30)  # Field name made lowercase.
    incent2per = models.SmallIntegerField(db_column='Incent2Per')  # Field name made lowercase.
    key4graph = models.BigIntegerField(db_column='Key4Graph', blank=True, null=True)  # Field name made lowercase.
    pattitle = models.CharField(db_column='PatTitle', max_length=10)  # Field name made lowercase.
    extopdno = models.CharField(db_column='ExtOPDNo', max_length=20)  # Field name made lowercase.
    extipdno = models.CharField(db_column='ExtIPDNo', max_length=20)  # Field name made lowercase.
    extreqno = models.CharField(db_column='ExtReqNo', max_length=20)  # Field name made lowercase.
    extbillno = models.CharField(db_column='ExtBillNo', max_length=20)  # Field name made lowercase.
    extpatcatg = models.CharField(db_column='ExtPatCatg', max_length=20)  # Field name made lowercase.
    extsmpcoldt = models.CharField(db_column='ExtSmpColDt', max_length=20)  # Field name made lowercase.
    extother = models.CharField(db_column='ExtOther', max_length=20)  # Field name made lowercase.
    salesrep = models.CharField(db_column='SalesRep', max_length=50)  # Field name made lowercase.
    reporeadysmssent = models.DateTimeField(db_column='RepoReadySMSSent', blank=True, null=True)  # Field name made lowercase.
    testresultsmssent = models.DateTimeField(db_column='TestResultSMSSent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLab'


class Tblpat(models.Model):
    patid = models.CharField(db_column='PatID', primary_key=True, max_length=10)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=20)  # Field name made lowercase.
    mname = models.CharField(db_column='MName', max_length=20)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=20)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB')  # Field name made lowercase.
    dobacc = models.BooleanField(db_column='DOBAcc')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=120)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=20)  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=20)  # Field name made lowercase.
    pin = models.CharField(db_column='PIN', max_length=6)  # Field name made lowercase.
    phresi = models.CharField(db_column='PhResi', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phoff = models.CharField(db_column='PhOff', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='eMail', max_length=50)  # Field name made lowercase.
    rh = models.CharField(db_column='Rh', max_length=1)  # Field name made lowercase.
    abo = models.CharField(db_column='ABO', max_length=2)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=10)  # Field name made lowercase.
    dor = models.DateTimeField(db_column='DOR')  # Field name made lowercase.
    foc = models.BooleanField(db_column='FOC')  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=10)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=50)  # Field name made lowercase.
    diabetic = models.BooleanField(db_column='Diabetic')  # Field name made lowercase.
    married = models.DateTimeField(db_column='Married', blank=True, null=True)  # Field name made lowercase.
    spouse = models.CharField(db_column='Spouse', max_length=30)  # Field name made lowercase.
    acckey = models.ForeignKey(Mstacc, models.DO_NOTHING, db_column='AccKey')  # Field name made lowercase.
    mobile4sms = models.CharField(db_column='Mobile4SMS', max_length=12)  # Field name made lowercase.
    validupto = models.DateTimeField(db_column='ValidUpto', blank=True, null=True)  # Field name made lowercase.
    iswebactive = models.BooleanField(db_column='IsWebActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPat'


class Tblpatimages(models.Model):
    imgkey = models.AutoField(db_column='ImgKey', primary_key=True)  # Field name made lowercase.
    labkey = models.ForeignKey(Tbllab, models.DO_NOTHING, db_column='LabKey')  # Field name made lowercase.
    imagefile = models.CharField(db_column='ImageFile', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPatImages'


class Tblpay(models.Model):
    paykey = models.AutoField(db_column='PayKey', primary_key=True)  # Field name made lowercase.
    labkey = models.ForeignKey(Tbllab, models.DO_NOTHING, db_column='LabKey')  # Field name made lowercase.
    paidon = models.DateTimeField(db_column='PaidOn')  # Field name made lowercase.
    recpno = models.IntegerField(db_column='RecpNo')  # Field name made lowercase.
    amount = models.SmallIntegerField(db_column='Amount')  # Field name made lowercase.
    cash = models.BooleanField(db_column='Cash')  # Field name made lowercase.
    chqno = models.CharField(db_column='ChqNo', max_length=20)  # Field name made lowercase.
    chqdate = models.DateTimeField(db_column='ChqDate', blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=30)  # Field name made lowercase.
    printed = models.SmallIntegerField(db_column='Printed')  # Field name made lowercase.
    oprkey = models.IntegerField(db_column='OPRKey')  # Field name made lowercase.
    paymode = models.SmallIntegerField(db_column='PayMode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPay'


class Tblrs232(models.Model):
    rs232pk = models.BigAutoField(db_column='RS232PK', primary_key=True)  # Field name made lowercase.
    instno = models.SmallIntegerField(db_column='InstNo')  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=10)  # Field name made lowercase.
    uniquemcno = models.CharField(db_column='UniqueMCNo', max_length=10)  # Field name made lowercase.
    sampleno = models.CharField(db_column='SampleNo', max_length=20)  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=5)  # Field name made lowercase.
    testdate = models.DateTimeField(db_column='TestDate')  # Field name made lowercase.
    patname = models.CharField(db_column='PatName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRS232'


class Tblrs232Err(models.Model):
    errpk = models.AutoField(db_column='ErrPK', primary_key=True)  # Field name made lowercase.
    instno = models.SmallIntegerField(db_column='InstNo')  # Field name made lowercase.
    errdate = models.DateTimeField(db_column='ErrDate')  # Field name made lowercase.
    errdesc = models.CharField(db_column='ErrDesc', max_length=8000)  # Field name made lowercase.
    errstring = models.CharField(db_column='ErrString', max_length=8000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRS232Err'


class Tblrs232Histo(models.Model):
    histopk = models.BigAutoField(db_column='HistoPK', primary_key=True)  # Field name made lowercase.
    rs232fk = models.ForeignKey(Tblrs232, models.DO_NOTHING, db_column='RS232FK')  # Field name made lowercase.
    component = models.CharField(db_column='Component', max_length=3, blank=True, null=True)  # Field name made lowercase.
    hdata = models.SmallIntegerField(db_column='HData', blank=True, null=True)  # Field name made lowercase.
    wbc = models.SmallIntegerField(db_column='WBC', blank=True, null=True)  # Field name made lowercase.
    rbc = models.SmallIntegerField(db_column='RBC', blank=True, null=True)  # Field name made lowercase.
    plt = models.SmallIntegerField(db_column='PLT', blank=True, null=True)  # Field name made lowercase.
    plt2 = models.SmallIntegerField(db_column='PLT2', blank=True, null=True)  # Field name made lowercase.
    imgpath = models.CharField(db_column='ImgPath', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRS232Histo'


class Tblrs232Histoimg(models.Model):
    rs232fk = models.ForeignKey(Tblrs232, models.DO_NOTHING, db_column='RS232FK', primary_key=True)  # Field name made lowercase.
    graph1 = models.BinaryField(db_column='Graph1', blank=True, null=True)  # Field name made lowercase.
    label1 = models.CharField(db_column='Label1', max_length=20)  # Field name made lowercase.
    graph2 = models.BinaryField(db_column='Graph2', blank=True, null=True)  # Field name made lowercase.
    label2 = models.CharField(db_column='Label2', max_length=20)  # Field name made lowercase.
    graph3 = models.BinaryField(db_column='Graph3', blank=True, null=True)  # Field name made lowercase.
    label3 = models.CharField(db_column='Label3', max_length=20)  # Field name made lowercase.
    graph4 = models.BinaryField(db_column='Graph4', blank=True, null=True)  # Field name made lowercase.
    label4 = models.CharField(db_column='Label4', max_length=20)  # Field name made lowercase.
    graph5 = models.BinaryField(db_column='Graph5', blank=True, null=True)  # Field name made lowercase.
    label5 = models.CharField(db_column='Label5', max_length=20)  # Field name made lowercase.
    graph6 = models.BinaryField(db_column='Graph6', blank=True, null=True)  # Field name made lowercase.
    label6 = models.CharField(db_column='Label6', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRS232HistoImg'


class Tblrs232Query(models.Model):
    querypk = models.BigAutoField(db_column='QueryPK', primary_key=True)  # Field name made lowercase.
    instno = models.SmallIntegerField(db_column='InstNo')  # Field name made lowercase.
    qryframe = models.CharField(db_column='QryFrame', max_length=8000)  # Field name made lowercase.
    qrydatetime = models.DateTimeField(db_column='QryDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRS232Query'


class Tblrs232Tests(models.Model):
    testpk = models.BigAutoField(db_column='TestPK', primary_key=True)  # Field name made lowercase.
    rs232fk = models.ForeignKey(Tblrs232, models.DO_NOTHING, db_column='RS232FK')  # Field name made lowercase.
    test = models.CharField(db_column='Test', max_length=15)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=50)  # Field name made lowercase.
    flag = models.CharField(db_column='Flag', max_length=5)  # Field name made lowercase.
    verified = models.DateTimeField(db_column='Verified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRS232Tests'


class Tblrecp(models.Model):
    recpkey = models.AutoField(db_column='RecpKey', primary_key=True)  # Field name made lowercase.
    acckey = models.ForeignKey(Mstacc, models.DO_NOTHING, db_column='AccKey')  # Field name made lowercase.
    recpno = models.IntegerField(db_column='RecpNo')  # Field name made lowercase.
    recpdate = models.DateTimeField(db_column='RecpDate')  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=30)  # Field name made lowercase.
    chqno = models.CharField(db_column='ChqNo', max_length=15)  # Field name made lowercase.
    chqdate = models.DateTimeField(db_column='ChqDate', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tds = models.DecimalField(db_column='TDS', max_digits=10, decimal_places=4)  # Field name made lowercase.
    oprkey = models.IntegerField(db_column='OPRKey')  # Field name made lowercase.
    printed = models.BooleanField(db_column='Printed')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=60)  # Field name made lowercase.
    particular = models.CharField(db_column='Particular', max_length=1000)  # Field name made lowercase.
    postdate = models.DateTimeField(db_column='PostDate', blank=True, null=True)  # Field name made lowercase.
    postby = models.IntegerField(db_column='PostBy', blank=True, null=True)  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRecp'


class Tblregi(models.Model):
    Tblregipk = models.SmallIntegerField(db_column='PK', primary_key=True)  # Field name made lowercase.
    doi = models.DateTimeField(db_column='DOI')  # Field name made lowercase.
    lockno = models.CharField(db_column='LockNo', max_length=15)  # Field name made lowercase.
    lanusers = models.SmallIntegerField(db_column='LANUsers')  # Field name made lowercase.
    remoteusers = models.SmallIntegerField(db_column='RemoteUsers')  # Field name made lowercase.
    instruments = models.CharField(db_column='Instruments', max_length=100)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=100)  # Field name made lowercase.
    custname = models.CharField(db_column='CustName', max_length=120)  # Field name made lowercase.
    addr = models.CharField(db_column='Addr', max_length=255)  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=50)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=30)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRegi'


class Tblrepo(models.Model):
    repokey = models.AutoField(db_column='RepoKey', primary_key=True)  # Field name made lowercase.
    labkey = models.ForeignKey(Tbllab, models.DO_NOTHING, db_column='LabKey')  # Field name made lowercase.
    repoid = models.CharField(db_column='RepoID', max_length=10)  # Field name made lowercase.
    prefix = models.CharField(db_column='PreFix', max_length=3)  # Field name made lowercase.
    repono = models.IntegerField(db_column='RepoNo')  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=2)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    rtfdata = models.CharField(db_column='RTFData', max_length=8000)  # Field name made lowercase.
    repogrp = models.CharField(db_column='RepoGrp', max_length=20)  # Field name made lowercase.
    delivby = models.IntegerField(db_column='DelivBy', blank=True, null=True)  # Field name made lowercase.
    delivat = models.DateTimeField(db_column='DelivAt', blank=True, null=True)  # Field name made lowercase.
    printed = models.SmallIntegerField(db_column='Printed')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    printhisto = models.BooleanField(db_column='PrintHisto')  # Field name made lowercase.
    smsstatus = models.CharField(db_column='SMSStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    emailsent = models.BooleanField(db_column='EmailSent')  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    printedby = models.IntegerField(db_column='PrintedBy', blank=True, null=True)  # Field name made lowercase.
    printdt = models.DateTimeField(db_column='PrintDt', blank=True, null=True)  # Field name made lowercase.
    entryby = models.IntegerField(db_column='EntryBy', blank=True, null=True)  # Field name made lowercase.
    entrydt = models.DateTimeField(db_column='EntryDt', blank=True, null=True)  # Field name made lowercase.
    verifyby = models.IntegerField(db_column='VerifyBy', blank=True, null=True)  # Field name made lowercase.
    verifydt = models.DateTimeField(db_column='VerifyDt', blank=True, null=True)  # Field name made lowercase.
    includeheader = models.BooleanField(db_column='IncludeHeader')  # Field name made lowercase.
    includefooter = models.BooleanField(db_column='IncludeFooter')  # Field name made lowercase.
    #repoprenosuf is disabled as it donot allow to run views.encounter=>reportpg.save() line to execute as this field is compund field
    #repoprenosuf = models.CharField(db_column='RepoPreNoSuf', max_length=15, blank=True, null=True)  # Field name made lowercase.
    webupstat = models.CharField(db_column='WebUpStat', max_length=1)  # Field name made lowercase.
    tatinmm = models.SmallIntegerField(db_column='TATinMM')  # Field name made lowercase.
    samplefk = models.IntegerField(db_column='SampleFK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRepo'
        unique_together = (('labkey', 'repoid'),)


class Tblsms(models.Model):
    smspk = models.AutoField(db_column='SMSPk', primary_key=True)  # Field name made lowercase.
    labkey = models.IntegerField(db_column='LabKey')  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=32)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate')  # Field name made lowercase.
    oprid = models.CharField(db_column='OPRID', max_length=5)  # Field name made lowercase.
    mobileno = models.CharField(db_column='MobileNo', max_length=15)  # Field name made lowercase.
    sms = models.CharField(db_column='SMS', max_length=4500)  # Field name made lowercase.
    refidno = models.CharField(db_column='RefIDNo', max_length=20)  # Field name made lowercase.
    sent2name = models.CharField(db_column='Sent2Name', max_length=62)  # Field name made lowercase.
    sent2type = models.CharField(db_column='Sent2Type', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    sentdate = models.DateTimeField(db_column='SentDate', blank=True, null=True)  # Field name made lowercase.
    msgseqno = models.SmallIntegerField(db_column='MsgSeqNo')  # Field name made lowercase.
    responseid = models.CharField(db_column='ResponseID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    msgtype = models.CharField(db_column='MsgType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    deliverystatus = models.CharField(db_column='DeliveryStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    response = models.CharField(db_column='Response', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSMS'
        unique_together = (('guid', 'msgseqno'),)


class Tblsms2Send(models.Model):
    sentsmspk = models.AutoField(db_column='SentSMSPk', primary_key=True)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=30)  # Field name made lowercase.
    mobileno = models.CharField(db_column='MobileNo', max_length=15)  # Field name made lowercase.
    sms = models.CharField(db_column='SMS', max_length=255)  # Field name made lowercase.
    sentfrom = models.CharField(db_column='SentFrom', max_length=20)  # Field name made lowercase.
    sentdate = models.DateTimeField(db_column='SentDate', blank=True, null=True)  # Field name made lowercase.
    oprid = models.CharField(db_column='OprID', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSMS2Send'


class Tblsmssent(models.Model):
    smspk = models.AutoField(db_column='SMSPk', primary_key=True)  # Field name made lowercase.
    senttime = models.DateTimeField(db_column='SentTime')  # Field name made lowercase.
    labrefno = models.CharField(db_column='LabRefNo', max_length=17)  # Field name made lowercase.
    patname = models.CharField(db_column='PatName', max_length=40)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=20)  # Field name made lowercase.
    drname = models.CharField(db_column='DrName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=800)  # Field name made lowercase.
    sentto = models.CharField(db_column='SentTo', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSMSSent'


class Tblsample(models.Model):
    samplekey = models.AutoField(db_column='SampleKey', primary_key=True)  # Field name made lowercase.
    labkey = models.ForeignKey(Tbllab, models.DO_NOTHING, db_column='LabKey')  # Field name made lowercase.
    sample = models.CharField(db_column='Sample', max_length=120)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    onat = models.DateTimeField(db_column='OnAt', blank=True, null=True)  # Field name made lowercase.
    tubecolor = models.CharField(db_column='TubeColor', max_length=8)  # Field name made lowercase.
    barcodeid = models.CharField(db_column='BarCodeID', max_length=15)  # Field name made lowercase.
    samplesuffix = models.CharField(db_column='SampleSuffix', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSample'


class Tblstkissitems(models.Model):
    issueitemkey = models.AutoField(db_column='IssueItemKey', primary_key=True)  # Field name made lowercase.
    issuekey = models.ForeignKey('Tblstkissue', models.DO_NOTHING, db_column='IssueKey')  # Field name made lowercase.
    mstitemkey = models.IntegerField(db_column='mstItemKey')  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty')  # Field name made lowercase.
    issuerate = models.DecimalField(db_column='IssueRate', max_digits=10, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStkIssItems'


class Tblstkissue(models.Model):
    issuekey = models.AutoField(db_column='IssueKey', primary_key=True)  # Field name made lowercase.
    issuedate = models.DateTimeField(db_column='IssueDate')  # Field name made lowercase.
    issuetime = models.CharField(db_column='IssueTime', max_length=5)  # Field name made lowercase.
    idt = models.DateTimeField(db_column='IDT', blank=True, null=True)  # Field name made lowercase.
    issrefno = models.CharField(db_column='IssRefNo', max_length=10)  # Field name made lowercase.
    issuetype = models.CharField(db_column='IssueType', max_length=15)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStkIssue'


class Tblstkpuritems(models.Model):
    puritemkey = models.AutoField(db_column='PurItemKey', primary_key=True)  # Field name made lowercase.
    purkey = models.ForeignKey('Tblstkpurchase', models.DO_NOTHING, db_column='PurKey')  # Field name made lowercase.
    mstitemkey = models.IntegerField(db_column='MstItemKey')  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=10, decimal_places=4)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=10, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStkPurItems'


class Tblstkpurchase(models.Model):
    purkey = models.AutoField(db_column='PurKey', primary_key=True)  # Field name made lowercase.
    purdate = models.DateTimeField(db_column='PurDate')  # Field name made lowercase.
    purtime = models.CharField(db_column='PurTime', max_length=5)  # Field name made lowercase.
    pdt = models.DateTimeField(db_column='PDT', blank=True, null=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=15)  # Field name made lowercase.
    party = models.CharField(db_column='Party', max_length=40)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStkPurchase'


class Tbltallycash(models.Model):
    trndate = models.DateTimeField(db_column='TrnDate', primary_key=True)  # Field name made lowercase.
    trntype = models.CharField(db_column='TrnType', max_length=1)  # Field name made lowercase.
    cashchq = models.CharField(db_column='CashChq', max_length=1)  # Field name made lowercase.
    acckey = models.IntegerField(db_column='AccKey')  # Field name made lowercase.
    accname = models.CharField(db_column='AccName', max_length=50)  # Field name made lowercase.
    postamt = models.IntegerField(db_column='PostAmt')  # Field name made lowercase.
    postdate = models.DateTimeField(db_column='PostDate')  # Field name made lowercase.
    postby = models.IntegerField(db_column='PostBy')  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTallyCash'
        unique_together = (('trndate', 'trntype', 'cashchq', 'acckey'),)


class Tbltallyexp(models.Model):
    trndate = models.DateTimeField(db_column='TrnDate', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=50)  # Field name made lowercase.
    ledgname = models.CharField(db_column='LedgName', max_length=50)  # Field name made lowercase.
    postamt = models.IntegerField(db_column='PostAmt')  # Field name made lowercase.
    postdate = models.DateTimeField(db_column='PostDate')  # Field name made lowercase.
    postby = models.IntegerField(db_column='PostBy')  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID')  # Field name made lowercase.
    vchnos = models.CharField(db_column='VchNos', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTallyExp'
        unique_together = (('trndate', 'category'),)


class Tbltests(models.Model):
    testkey = models.AutoField(db_column='TestKey', primary_key=True)  # Field name made lowercase.
    invkey = models.ForeignKey(Tblinv, models.DO_NOTHING, db_column='InvKey')  # Field name made lowercase.
    repokey = models.ForeignKey(Tblrepo, models.DO_NOTHING, db_column='RepoKey')  # Field name made lowercase.
    test = models.CharField(db_column='Test', max_length=100)  # Field name made lowercase.
    testid = models.CharField(db_column='TestID', max_length=10)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=180)  # Field name made lowercase.
    options = models.CharField(db_column='Options', max_length=5000)  # Field name made lowercase.
    analyzer = models.CharField(db_column='Analyzer', max_length=10)  # Field name made lowercase.
    anatest = models.CharField(db_column='AnaTest', max_length=10)  # Field name made lowercase.
    normals = models.CharField(db_column='Normals', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    oprkey = models.IntegerField(db_column='OPRKey', blank=True, null=True)  # Field name made lowercase.
    nlow = models.DecimalField(db_column='nLow', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nhigh = models.DecimalField(db_column='nHigh', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dept = models.CharField(db_column='Dept', max_length=10)  # Field name made lowercase.
    eorder = models.SmallIntegerField(db_column='EOrder')  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=200)  # Field name made lowercase.
    vrule = models.CharField(db_column='VRule', max_length=200)  # Field name made lowercase.
    vmsg = models.CharField(db_column='VMsg', max_length=30)  # Field name made lowercase.
    printincard = models.BooleanField(db_column='PrintInCard')  # Field name made lowercase.
    uploaded = models.BooleanField(db_column='Uploaded')  # Field name made lowercase.
    test4sms = models.CharField(db_column='Test4SMS', max_length=50)  # Field name made lowercase.
    smsstatus = models.CharField(db_column='SMSStatus', max_length=1)  # Field name made lowercase.
    calctest = models.BooleanField(db_column='CalcTest')  # Field name made lowercase.
    vrulemust = models.BooleanField(db_column='VRuleMust')  # Field name made lowercase.
    visible2all = models.BooleanField(db_column='Visible2All')  # Field name made lowercase.
    tatinmm = models.SmallIntegerField(db_column='TATinMM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTests'


class Tbltestscalc(models.Model):
    repokey = models.ForeignKey(Tblrepo, models.DO_NOTHING, db_column='RepoKey', primary_key=True)  # Field name made lowercase.
    condorder = models.SmallIntegerField(db_column='CondOrder')  # Field name made lowercase.
    ifcond = models.CharField(db_column='IfCond', max_length=5000)  # Field name made lowercase.
    trueval = models.CharField(db_column='TrueVal', max_length=180)  # Field name made lowercase.
    falseval = models.CharField(db_column='FalseVal', max_length=180)  # Field name made lowercase.
    calctestid = models.CharField(db_column='CalcTestID', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTestsCalc'
        unique_together = (('repokey', 'condorder'),)


class Tblupdate(models.Model):
    updpk = models.AutoField(db_column='UpdPk', primary_key=True)  # Field name made lowercase.
    execdate = models.DateTimeField(db_column='ExecDate')  # Field name made lowercase.
    verdate = models.DateTimeField(db_column='VerDate')  # Field name made lowercase.
    vernum = models.CharField(db_column='VerNum', max_length=15)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUpdate'


class Tblvisits(models.Model):
    visitkey = models.AutoField(db_column='VisitKey', primary_key=True)  # Field name made lowercase.
    visitid = models.IntegerField(db_column='VisitID')  # Field name made lowercase.
    labkey = models.ForeignKey(Tbllab, models.DO_NOTHING, db_column='LabKey', blank=True, null=True)  # Field name made lowercase.
    visiton = models.DateTimeField(db_column='VisitON')  # Field name made lowercase.
    visitby = models.IntegerField(db_column='VisitBy', blank=True, null=True)  # Field name made lowercase.
    rs2visitor = models.SmallIntegerField(db_column='Rs2Visitor')  # Field name made lowercase.
    patname = models.CharField(db_column='PatName', max_length=40)  # Field name made lowercase.
    addr = models.CharField(db_column='Addr', max_length=120)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20)  # Field name made lowercase.
    visited = models.DateTimeField(db_column='Visited', blank=True, null=True)  # Field name made lowercase.
    oprkey = models.IntegerField(db_column='OPRKey')  # Field name made lowercase.
    inv = models.CharField(db_column='Inv', max_length=100)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVisits'


class Tblwebrepo(models.Model):
    webrepopk = models.AutoField(db_column='WebRepoPK', primary_key=True)  # Field name made lowercase.
    labkey = models.IntegerField(db_column='LabKey')  # Field name made lowercase.
    repokey = models.IntegerField(db_column='RepoKey')  # Field name made lowercase.
    repoid = models.CharField(db_column='RepoID', max_length=10)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate')  # Field name made lowercase.
    statusflag = models.CharField(db_column='StatusFlag', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblWebRepo'


class Tblwordproc(models.Model):
    wordproccode = models.CharField(db_column='WordProcCode', primary_key=True, max_length=20)  # Field name made lowercase.
    wordproctext = models.TextField(db_column='WordProcText', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tblWordProc'


class Tmppatimages(models.Model):
    labkey = models.IntegerField(db_column='LabKey', primary_key=True)  # Field name made lowercase.
    image1 = models.BinaryField(db_column='Image1', blank=True, null=True)  # Field name made lowercase.
    image3 = models.BinaryField(db_column='Image3', blank=True, null=True)  # Field name made lowercase.
    image4 = models.BinaryField(db_column='Image4', blank=True, null=True)  # Field name made lowercase.
    image5 = models.BinaryField(db_column='Image5', blank=True, null=True)  # Field name made lowercase.
    image6 = models.BinaryField(db_column='Image6', blank=True, null=True)  # Field name made lowercase.
    image7 = models.BinaryField(db_column='Image7', blank=True, null=True)  # Field name made lowercase.
    image8 = models.BinaryField(db_column='Image8', blank=True, null=True)  # Field name made lowercase.
    image9 = models.BinaryField(db_column='Image9', blank=True, null=True)  # Field name made lowercase.
    image10 = models.BinaryField(db_column='Image10', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpPatImages'


class Tmpprinthisto(models.Model):
    Tmpprinthistoid = models.SmallIntegerField(db_column='ID')  # Field name made lowercase.
    header = models.CharField(db_column='Header', max_length=5000)  # Field name made lowercase.
    rtfdata = models.CharField(db_column='RTFData', max_length=8000)  # Field name made lowercase.
    footer = models.CharField(db_column='Footer', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpPrintHisto'


class Zdrvisits(models.Model):
    visitkey = models.AutoField(db_column='VisitKey', primary_key=True)  # Field name made lowercase.
    drkey = models.ForeignKey(Mstdr, models.DO_NOTHING, db_column='DrKey')  # Field name made lowercase.
    visitdate = models.DateTimeField(db_column='VisitDate')  # Field name made lowercase.
    visitnotes = models.CharField(db_column='VisitNotes', max_length=500)  # Field name made lowercase.
    drnotes = models.CharField(db_column='DrNotes', max_length=500)  # Field name made lowercase.
    drcomplain = models.CharField(db_column='DrComplain', max_length=500)  # Field name made lowercase.
    oprid = models.CharField(db_column='OPRID', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zDrVisits'
