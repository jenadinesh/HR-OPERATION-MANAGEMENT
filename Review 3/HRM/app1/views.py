from django.shortcuts import render
from django.views.generic import UpdateView

from .models import adminLogin, Employee, recuirtment, applicant, applicationform, Interviewschedule, Finalinterview


def Adminlogin(request):
    username=request.POST.get('name')
    password=request.POST.get('password')
    # e=adminLogin(username=username,password=password)
    # e.save()
    qs=adminLogin.objects.filter(username=username,password=password)
    if qs:
        return render(request,"Welcomeadmin.html")
    else:
        return render(request,"admin.html",{'message':'Invalid User'})


def createEmployee(request):
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    password=request.POST.get("password")
    des=request.POST.get("designation")
    address=request.POST.get("address")
    cno=request.POST.get("cno")
    email=request.POST.get("email")
    Employee(employeeid=idno,name=name,password=password,designation=des,address=address,cno=cno,email=email).save()
    return render(request,"addEmployee.html",{"msg":"EMPLOYEE ADDED SUCEESFULLY"})


def viewEmployee(request):
    qs=Employee.objects.all()
    return render(request,"Viewemployee.html",{'data':qs})


def updateemp(request):
    qs=Employee.objects.all()
    return render(request,"updateemp.html",{'data':qs})

def editemp(request):
    id=request.GET.get("id")
    qs=Employee.objects.filter(employeeid=id)
    return render(request,"editupdateemp.html",{'data':qs})

def saveUpdate(request):
    id=request.POST.get("idno")
    name=request.POST.get("name")
    password=request.POST.get("password")
    des=request.POST.get("des")
    add=request.POST.get("add")
    cno=request.POST.get("cno")
    email=request.POST.get("email")
    Employee(employeeid=id,name=name,password=password,designation=des,address=add,cno=cno,email=email).save()
    qs=Employee.objects.filter(employeeid=id)

    return render(request,"editupdateemp.html",{'data':qs},{"msg": "UPDATED SUCEESFULLY"})
def deleteemp(request):
    qs=Employee.objects.all()

    return render(request,"deleteemp.html",{'data':qs})

def deleteEMP(request):
    checkbox=request.POST.get("t1")
    Employee.objects.filter(employeeid=checkbox).delete()
    qs = Employee.objects.all()
    return render(request,"deleteemp.html",{'data':qs},{'msg':'employee deleted'})

def managerlogin(request):
    name=request.POST.get('name')
    password=request.POST.get('password')
    qs=Employee.objects.filter(name=name,password=password)
    if not  qs:
        return render(request, "manager.html", {'msg': 'InvalidEmployee'})
    else:
        return render(request, "managerloginpage.html")


def addnewrecuirtment(request):

    return render(request,"postnewrecuirtment.html")


def saverecemp(request):
    code=request.POST.get("t1")
    qul=request.POST.get("t2")
    start=request.POST.get("t3")
    age=request.POST.get("t4")
    last=request.POST.get("t5")
    id=request.POST.get("t6")
    nop=request.POST.get("t7")
    des=request.POST.get("t8")
    res=request.POST.get("t9")
    cno=request.POST.get("t10")
    recuirtment(oppcode=code,qualification=qul,startregistration=start,age=age,lastregistration=last,deptid=id,position=nop,description=des,responsibilities=res,cno=cno).save()

    return render(request,"postnewrecuirtment.html",{'msg':'ADDED RECUIRTMENT DETAILS SUCEESFULLY'})


def modifyRecuirtment(request):
    code=request.POST.get("t1")
    qs=recuirtment.objects.filter(oppcode=code)
    return render(request,"modifyrecuirtment.html",{'data':qs})
def deleterec(request):
    qs=recuirtment.objects.all()
    return render(request,"deletepost.html",{'data':qs})

def deletePost(request):
    checkbox = request.POST.get("t1")
    recuirtment.objects.filter(oppcode=checkbox).delete()
    qs = recuirtment.objects.all()
    return render(request, "deleteemp.html", {'data': qs}, {'msg': 'post deleted'})

def Getdetails(request):
    idno=request.POST.get("id")
    # applicationform.objects.all()
    qs1 = Employee.objects.all()
    qs = applicationform.objects.filter(id=idno)
    if qs:
        return render(request,"assigninginterview.html",{"data":qs,"res":qs1})
    else:
        return render(request,"interviewpage.html",{'msg':'Invalid applicant id'})

def interschedule(request):
    id1=request.POST.get("id1")
    empid=request.POST.get("id2")
    schdate=request.POST.get("d1")
    Interviewschedule(idno=id1,empid=empid,date=schdate).save()
    return render(request,"assigninginterview.html",{'msg':'INTERVIEW SCHEDULED SUCESSFULLY'})


def applicantRegister(request):
    return render(request,"applicantregisterpage.html")
def saveRegister(request):
    name = request.POST.get("a1")
    dob = request.POST.get("a2")
    email = request.POST.get("a3")
    gender = request.POST.get("a4")
    mob = request.POST.get("a5")
    address = request.POST.get("a6")
    username = request.POST.get("a7")
    password = request.POST.get("a8")
    applicant(name=name, dob=dob, email=email, gender=gender, mobile=mob, address=address, username=username,
              password=password).save()
    return render(request,"applicantregisterpage.html",{'msg':'Register successfully'})

def loginapplicant(request):
    username=request.POST.get("name")
    password=request.POST.get("password")
    qs=applicant.objects.filter(username=username,password=password)
    if qs:
        return render(request,"applicantloginpage.html")
    else:
        return render(request,"applicant.html",{'msg':'Invalid Applicant'})
def saveForm(request):
    name=request.POST.get("a1")
    dob=request.POST.get("a2")
    email=request.POST.get("a3")
    gender=request.POST.get("a4")
    mob=request.POST.get("a5")
    address=request.POST.get("a6")
    qual=request.POST.get("a7")
    post=request.POST.get("a8")
    percentage=request.POST.get("a9")
    resume=request.POST.get("a10")
    applicationform(name=name,dob=dob,email=email,gender=gender,mob=mob,address=address,qualification=qual,post=post,
                    percentage=percentage,resume=resume).save()
    return render(request,"applicantloginpage.html",{'msg':'SUCEESFULLY APPLIED'})

def hrHead(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    qs = Employee.objects.filter(name=name, password=password)
    qs1 = Finalinterview.objects.all()
    if not qs:
        return render(request, "Hrhead.html")
    else:
        return render(request, "Hrheadloginpage.html",{"res":qs1})

# def Shortlistemp(request):
#     qs=applicationform.objects.all()
#     if qs:
#         return render(request,"shortlistemp.html",{'data':qs})
#     else:
#         return render(request,"Hrheadloginpage.html")

def shortedapplicant(request):
    qs=applicationform.objects.all()
    qs1=Finalinterview.objects.all()
    if qs:
        return render(request,"shortlistapplicant.html",{'data':qs,'res':qs1})

def Selectedapplicant(request):
    qs=Finalinterview.objects.all()
    qs=Finalinterview.objects.filter()
    return render(request,"selectedemp.html",{'data':qs})

def Rejectedapplicant(request):
    qs=Finalinterview.objects.all()
    return render(request,"rejectedapplicant.html",{'data':qs})


def Interviewerlogin(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    qs = Employee.objects.filter(name=name, password=password)
    if not qs:
        return render(request, "interviewer.html", {'msg': 'Invalid Employee'})
    else:
        return render(request, "interviewerhomepage.html")

def getInterviewid(request):
    qs1 = applicationform.objects.all()
    qs=Interviewschedule.objects.all()
    return render(request,"getapplicant.html",{'data':qs,"data2":qs1})


def displayemployees(request):
    af=applicationform.objects.all()
    return render(request,"interviewpage.html",{"data":af})

def getDetails(request):
    idno2 = request.POST.get("id1")
    qs =Interviewschedule.objects.filter(idno=idno2)

    if qs:
        return render(request, "finalinterview.html", {"data":qs})
    else:
        return render(request, "finalinterview.html", {'msg': 'data is not there'})

def Setinterview(request):
    interid=request.POST.get("id1")
    inter=request.POST.get("id2")
    sche=request.POST.get("id3")
    apid=request.POST.get("id4")
    print(apid)
    result=request.POST.get("id5")
    Finalinterview(inter_id=interid,interviewer=inter,schedule=sche,appid=apid,res=result).save()
    return render(request,"heading.html",{'msg':'Data is saved'})