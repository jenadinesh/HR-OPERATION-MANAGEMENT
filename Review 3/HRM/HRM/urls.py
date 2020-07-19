"""HRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, ListView
from app1.models import applicationform

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',TemplateView.as_view(template_name="heading.html"),name='index'),
    #homepage
    path('home/',TemplateView.as_view(template_name="heading.html")),
    #Adminpage
    path('adminpage/',TemplateView.as_view(template_name="admin.html")),
    path('welcomeadmin/',views.Adminlogin),
    path('addemployee/',TemplateView.as_view(template_name="addEmployee.html")),
    path('logout/',TemplateView.as_view(template_name="admin.html")),
    #AddEmployeepage
    path('employeecreate/',views.createEmployee),
    path('viewemployee/',views.viewEmployee),
    path('updateemployee/',views.updateemp),
    path('editemp/',views.editemp),
    path('saveupdate/',views.saveUpdate),
    path('deleteemployee/',views.deleteemp),
    path('delete/',views.deleteEMP),
    #Managerpage
    path('manager/',TemplateView.as_view(template_name="manager.html")),
    path('welcomemanager/',views.managerlogin,name='manager_login'),
    path('logoutm/',TemplateView.as_view(template_name="manager.html")),
    #Recuirtment
    path('recuirtment/',TemplateView.as_view(template_name="Recuirtmentpage.html")),
    path('addrec/',views.addnewrecuirtment),
    path('saverec/',views.saverecemp),
    path('modify/',TemplateView.as_view(template_name="Recuirtmentmodifypage.html")),
    path('modifyrec/',views.modifyRecuirtment),
    path('deletep/',views.deleterec),
    path('deletepost/',views.deletePost),
    #interview schedule
    path('interviews/',views.displayemployees),
    path('showdetails/',views.Getdetails),
    path('schedule/',views.interschedule),
    #applicant
    path('applicant/',TemplateView.as_view(template_name="applicant.html")),
    path('applicantregister/',views.applicantRegister),
    path('saveregister/',views.saveRegister),
    path('applicantlogin/',views.loginapplicant),
    path('formsave/',views.saveForm),
    path('loogouta/',TemplateView.as_view(template_name="applicant.html")),
    #hrhead
    path('hrhead/',TemplateView.as_view(template_name="Hrhead.html")),
    path('hrheadlogin/',views.hrHead),
    # path('shortlist/',views.Shortlistemp),
    path('shortlist1/',views.shortedapplicant),
    path('vselected/',views.Selectedapplicant),
    path('vrejected/',views.Rejectedapplicant),
    path('logouth/',TemplateView.as_view(template_name="Hrhead.html")),
    #interviewer
    path('interviewer/',TemplateView.as_view(template_name="interviewer.html")),
    path('loginint/',views.Interviewerlogin),
    path('selection/',views.getInterviewid),
    path('getid/',views.getDetails),
    path('setinterview/',views.Setinterview),
    path('logouti/',TemplateView.as_view(template_name="interviewer.html")),
]
