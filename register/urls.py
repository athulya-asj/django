from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns=[
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('adminpage/',TemplateView.as_view(template_name='adminpage.html'),name='adminpage'),
    #path('submit/',views.display,name='submit'),
    path('admin',views.authentication,name='submit'),
    #path('addfact/',TemplateView.as_view(template_name='addfact.html'),name='addfact'),
    path('facultyreg/',TemplateView.as_view(template_name='facultyreg.html'),name='facultyreg'),
    path('fact',TemplateView.as_view(template_name='fact.html'),name='fact'),
    path('studentreg/',TemplateView.as_view(template_name='studentreg.html'),name='studentreg'),
    path('studaattent/',TemplateView.as_view(template_name='stdattend.html'),name='stdattend'),
    path('apply-leave/',TemplateView.as_view(template_name='leave.html'),name='leave'),
    path('factapply-leave/',TemplateView.as_view(template_name='factleave.html'),name='factleave'),
    path('fact-attendance/',TemplateView.as_view(template_name='factattend.html'),name='factattend'),
    path('studentmark/',TemplateView.as_view(template_name='studentmark.html'),name='studentmark'),
    path('mydetails/',TemplateView.as_view(template_name='personaldetails.html'),name='personaldetails'),
    path('student/',TemplateView.as_view(template_name='student.html'),name='student'),
    path('mymarks/',TemplateView.as_view(template_name='marks.html'),name='marks'),
    path('mystud/',TemplateView.as_view(template_name='studntview.html'),name='view'),
    path('pass/',TemplateView.as_view(template_name='password.html'),name='password'),
    path('mob/',TemplateView.as_view(template_name='mobile.html'),name='mobile'),
    path('e-mail/',TemplateView.as_view(template_name='email.html'),name='email'),
    path('',TemplateView.as_view(template_name='logout.html'),name='logout'),
   

    path('faculty_reg',views.addfactsignup,name='facultyregist'),
    path('studentreg',views.signupstud,name='stdregistration'),
    path('stdattn/',views.studattan,name='stdattantance'),
    path('leave/',views.leaveapp,name='leave_ap'),
    path('addfact',views.addfaculty,name='addfact'), 
    path('fact_leav',views.leavefaculty,name='factleave'), 
    path('fact_attendance',views.facultattendence,name='factattend'),
    path('studentmark',views.stdmark,name='studentmark'),
    path('personaldetails',views.detailsstudent,name='personaldetails'),
    path('markdetails/',views.markview,name='marks'),
    path('studentdetails/',views.studview,name='view_stud'),
    path('facdetails/',views.facview,name='viewfac'),
]