from django.db import models

class admin(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class faculty(models.Model):
     name=models.CharField(max_length=30,null=True,blank=True)
     password=models.CharField(max_length=30,null=True,blank=True) 
class meta: 
     db_table="register_faculty" 
class factsignup(models.Model):
    factid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    dob=models.DateField(max_length=10)
    gender=models.CharField(max_length=20)
    qualification=models.CharField(max_length=30)
    mobile=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=30)
    assbatch=models.CharField(max_length=30)
class meta: 
     db_table="register_facultysignup"     

class student(models.Model):
    stdid=models.IntegerField(primary_key=True)
    admnno=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    dob=models.DateField(max_length=10)
    gender=models.CharField(max_length=20)
    mobile=models.IntegerField(null=True,blank=True)
    admdate=models.DateField(max_length=20)
    guardian=models.CharField(max_length=20)
    batch=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30,null=True)
class meta: 
     db_table="register_student"   

class studentattendence(models.Model):
    stdid=models.IntegerField(null=True,blank=True)
    date=models.DateField(max_length=10)
    name=models.CharField(max_length=20)
    hours1status=models.CharField(max_length=10)
    hours2status=models.CharField(max_length=10)
    hours3status=models.CharField(max_length=10)
    hours4status=models.CharField(max_length=10)   

class applyleave(models.Model):
    name=models.CharField(max_length=20)
    to=models.CharField(max_length=20)   
    leavereason=models.CharField(max_length=20) 
    fromdate=models.DateField(max_length=10)
    todate=models.DateField(max_length=10)  
    class meta:
        db_table="register_leaveapp"     

class factattend( models.Model):
    factid=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=20)
    date=models.DateField(max_length=10)
    hours1status=models.CharField(max_length=10)
    hours2status=models.CharField(max_length=10)
    hours3status=models.CharField(max_length=10)
class meta:
    db_table="register_factattendance" 

class leavefact(models.Model):
    name=models.CharField(max_length=20)
    to=models.CharField(max_length=20)   
    leavereason=models.CharField(max_length=20) 
    fromdate=models.DateField(max_length=10)
    todate=models.DateField(max_length=10)  
class meta:
    db_table="register_leavefact"             

class studentmark(models.Model):
    stdid=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=20)
    assessmentno=models.IntegerField(null=True,blank=True)
    sub1mark=models.IntegerField(null=True,blank=True)
    sub2mark=models.IntegerField(null=True,blank=True)
    sub3mark=models.IntegerField(null=True,blank=True)
    percentage=models.IntegerField(null=True,blank=True)
class meta:
    db_table="register_stdentmrk"     