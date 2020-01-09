from django.shortcuts import render
from register.models import admin
from register.models import faculty 
from register.models import student,factsignup,student,studentattendence
from register.models import applyleave,factattend
from register.models import leavefact,studentmark

from django.http import HttpResponse

def display (request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        a=admin(username=username,password=password,)
        a.save()
    return render(request,'adminpage.html')   

def authentication(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u= admin.objects.filter(username=username,password=password)
        c=0
        if u.count()==1 :
            return render(request,'adminpage.html')
        else:
            u=faculty.objects.filter(name=username,password=password)
            if u.count()==1 :
                return render(request,'fact.html')
            else:
                u2=student.objects.filter(name=username,password=password)
                if u2.count()==1:
                    request.session['user']=username
                    qry=student.objects.all().filter(name=username)[0]
                    request.session['stid']=qry.stdid
                    return render(request,'student.html')
                else:
                    return HttpResponse('login unsucccessful')
def addfaculty(request):
    if request.method=="POST":
        name=request.POST.get('username')
        password=request.POST.get('password')
        b=faculty(name=name,password=password,)
        b.save()
    return render(request,'addfact.html')
def addfactsignup(request):    
    if request.method=="POST":
        factid=request.POST.get('factid')
        name=request.POST.get('name')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        qualification=request.POST.get('qualification')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        assbatch=request.POST.get('assbatch')
        c=factsignup(factid=factid,name=name,address=address,dob=dob,gender=gender,qualification=qualification,mobile=mobile,email=email,assbatch=assbatch)
        c.save()
    return render(request,'facultyreg.html')    
def signupstud(request):
    if request.method=='POST':
        stdid=request.POST.get('stdid')
        admnno=request.POST.get('admnno')
        name=request.POST.get('name')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mobile')
        admdate=request.POST.get('admdate')
        guardian=request.POST.get('guardian')
        batch=request.POST.get('batch')
        email=request.POST.get('email')
        password=request.POST.get('password')
        d=student(stdid=stdid,admnno=admnno,admdate=admdate,name=name,address=address,dob=dob,gender=gender,mobile=mobile,guardian=guardian,batch=batch,email=email,password=password)
        d.save()
    return render(request,'studentreg.html')

def studattan(request):
    if request.method=='POST':
        stdid=request.POST.get('stdid')
        name=request.POST.get('name')
        date=request.POST.get('date')
        hours1status=request.POST.get('hours1status')
        hours2status=request.POST.get('hours2status')
        hours3status=request.POST.get('hours3status')
        hours4status=request.POST.get('hours4status')
        e=studentattendence(stdid=stdid,date=date,name=name,hours1status=hours1status,
        hours2status=hours2status,hours3status=hours3status,hours4status=hours4status)
        e.save()
    return render(request,'stdattend.html')

def leaveapp(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        to=request.POST.get('to')
        leavereason=request.POST.get('leavereason')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate') 
        f=applyleave(name=name,to=to,leavereason=leavereason,fromdate=fromdate,todate=todate)
        f.save()
    return render(request,'leave.html')    

def facultattendence(request):
    if request.method=='POST':
        factid=request.POST.get('factid')
        name=request.POST.get('name')
        date=request.POST.get('date')
        hours1status=request.POST.get('hours1status')
        hours2status=request.POST.get('hours2status')
        hours3status=request.POST.get('hours3status')
        g=factattend(stdid=stdid,date=date,name=name,hours1status=hours1status,
        hours2status=hours2status,hours3status=hours3status)
        g.save()
    return render(request,'factattend.html')
        
def leavefaculty(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        to=request.POST.get('to')
        leavereason=request.POST.get('leavereason')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate') 
        h=leavefact(name=name,to=to,leavereason=leavereason,fromdate=fromdate,todate=todate)
        h.save()
    return render(request,'factleave.html')  

def stdmark(request):
    if request.method== 'POST':
        stdid=request.POST.get('stdid')
        name=request.POST.get('name')
        assessmentno=request.POST.get('assessmentno')
        sub1mark=request.POST.get('sub1mark')
        sub2mark=request.POST.get('sub2mark')
        sub3mark=request.POST.get('sub3mark')
        percentage=request.POST.get('percentage')
        i=studentmark(stdid=stdid,name=name,assessmentno=assessmentno,sub1mark=sub1mark,sub2mark=sub2mark,sub3mark=sub3mark,percentage=percentage)
        i.save()
    return render(request,'studentmark.html')    
   
def detailsstudent(request):
    queryset=student.objects.all().filter(name=request.session['user'])
    return render(request,'personaldetails.html',{'authors':queryset})

def markview(request):
    querysett=studentmark.objects.all().filter(stdid=request.session['stid'])
    return render(request,'marks.html',{'authorss':querysett})    

def studview(request):
    querysettttt=student.objects.all().filter()
    return render(request,'studntview.html',{'authorsssss':querysettttt})    

def facview(request):
    querysetttt=factsignup.objects.all().filter()
    return render(request,'viewfac.html',{'authorssss':querysetttt})    