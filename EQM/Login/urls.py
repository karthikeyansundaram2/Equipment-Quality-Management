from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls import patterns
from models import Login,Register
urlpatterns = [

  
   url(r'^$', views.LoginCreate.as_view(), name='login-add'),
   url(r'^register/',views.RegisterCreate.as_view(),name='register'),   
   url(r'^(?P<LoginId>[-\w]+)/(?P<Role>[-\w]+)/$', views.manager, name='manager'),
   url(r'^(?P<LoginId>[-\w]+)/(?P<Role>[-\w]+)/$', views.employee, name='employee'),
   url(r'^(?P<LoginId>[-\w]+)/(?P<Role>[-\w]+)/$',views.adminpage,name='adminpage'),
   url(r'^addmachines/',views.AddMachines.as_view(),name='addmachines'),
   url(r'^addemployee/',views.AddEmployee.as_view(),name='addemployee'),
   url(r'^addamc/',views.AddAMC.as_view(),name='addamc'),
   url(r'^changeallocation/',views.ChangeAllocation.as_view(),name='change'),
   url(r'^addemployeedetails/',views.AddEmployeeDetails.as_view(),name='addemployeedetails'),
   url(r'^viewmachinedetails/',views.viewmachinedetails,name='viewmachinedetails'),
   url(r'^addmanager/',views.addmanager.as_view(),name='addmanager'),
   url(r'^viewemployee/',views.viewemployee,name='viewemployee'),
   url(r'^viewamc/',views.viewamc,name='viewamc'),
   url(r'^sess/',views.adminpage,name='sess'),
   url(r'^logout/',views.logout,name='logout'),
   url(r'^updatemachine/',views.updatemachine,name='updatemachine'),
   url(r'^editmachine/',views.AddMachines.as_view(),name='editmachine'),
   url(r'^deletemachine/',views.deletemachine,name='deletemachine'),
   url(r'^updateamcwarranty/',views.updateamcwarranty,name='updatemcwarranty'),
]
