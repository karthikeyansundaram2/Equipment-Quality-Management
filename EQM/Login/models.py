from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from datetime import date
from django.utils.translation import gettext as _

ROLE = (
	('admin','ADMIN'),
	('employee','EMPLOYEE'),
	('manager','MANAGER'),
	)
Status=(
	('active','ACTIVE'),
	('ordered','ORDERED'),
	)
CurrentStatus=(
	('inuse','INUSE'),
	('idle','IDLE'),
	('underrepair','UNDER REPAIR'),
	('scrap','SCRAP'),
	('discoursed','DISCOURSED'),
	)

class Login(models.Model):

	LoginId = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
    
	Role = models.CharField(max_length=20, choices=ROLE, default='admin')
  
	def get_absolute_url(self):

		if self.Role == 'admin':
			#request.session['LoginId']='123'
			#return HttpResponse('hello'+request.session['LoginId'])  
			return reverse('adminpage',kwargs={'LoginId':self.LoginId, 'Role':self.Role})
			#model.addAttribute('LoginId',self.LoginId,'views.py')
		elif self.Role == 'employee':
			return reverse('employee',kwargs={'LoginId':self.LoginId, 'Role':self.Role})
		else:
			return reverse('manager',kwargs={'LoginId':self.LoginId, 'Role':self.Role})
	def __str__(self):
		return self.LoginId


			
 
    			
			
class Register(models.Model):
	AdminName=models.CharField(max_length=100)
	AdminID=models.CharField(max_length=100)
	Department=models.CharField(max_length=100)
	MobileNumber=models.CharField(max_length=10)
	password=models.CharField(max_length=50)
	
	def get_absolute_url(self):
		return reverse('login-add')


class AddMachine(models.Model):
	MachineName=models.CharField(max_length=100)
	Manufacturer=models.CharField(max_length=100)
	Model=models.CharField(max_length=100)
	SerialNumber=models.CharField(max_length=10)
	Status = models.CharField(max_length=20, choices=Status, default='')
	Category=models.CharField(max_length=50)
	OperatingSystem=models.CharField(max_length=50)
	
	EmployeeId=models.CharField(max_length=15)
	Location=models.CharField(max_length=45)
	Department=models.CharField(max_length=30)
	SupportLink=models.CharField(max_length=100)
	ServiceDate = models.DateField(_("Date"), default=date.today)
	


	Specification= models.CharField(max_length=300)
	PurchasePrice=models.CharField(max_length=100)
    

	Description=models.CharField(max_length=300)
    

	
	def get_absolute_url(self):
		return reverse('addmachines')

	def __str__(self):
		return 'Machine Name:'+ self.MachineName +'  Manufacturer: ' + self.Manufacturer + 'SerialNumber:'+self.SerialNumber+'Make:'+self.Make+'Status:'+self.Status + 'Support Link:'+self.SupportLink


    
class AddAMC(models.Model):
	Category=models.CharField(max_length=100)
	SubCategory=models.CharField(max_length=100)
	MachineName=models.CharField(max_length=100)
	Make=models.CharField(max_length=10)
	CurrentStatus = models.CharField(max_length=20, choices=CurrentStatus, default='')
    
	PurchaseDate = models.DateField(_("Date"), default=date.today)
	Vendor=models.CharField(max_length=100)
	Installationfees=models.CharField(max_length=100)

	Specification=models.CharField(max_length=300)

	def get_absolute_url(self):
		return reverse('addmachines')


class ChangeAllocation(models.Model):
    Category=models.CharField(max_length=100)
    SubCategory=models.CharField(max_length=100)
    EarlierAllocationDate = models.DateField(_("Date"), default=date.today)
    NewDepartment=models.CharField(max_length=25)
    ExistingDepartment=models.CharField(max_length=10)
    Status=models.CharField(max_length=20, choices=Status, default='')
    ExistingUser=models.CharField(max_length=50)
    NewUser=models.CharField(max_length=50)
    AllocationDate = models.DateField(_("Date"), default=date.today)
    MachineName=models.CharField(max_length=100)

    def get_absolute_url(self):
		return reverse('adminpage')
	





class AddEmployee(models.Model):
    EmployeeId=models.CharField(max_length=50)
    password=models.CharField(max_length=25)

    def get_absolute_url(Self):
    	return reverse('adminpage')

class AddEmployeeDetails(models.Model):
	EmployeeName=models.CharField(max_length=100)
	EmployeeId=models.CharField(max_length=100)
	Department=models.CharField(max_length=50)
	MobileNumber=models.CharField(max_length=10)
	password=models.CharField(max_length=50)

	def get_absolute_url(Self):
		return reverse('addemployeedetails')


class addmanager(models.Model):
	ManagerName=models.CharField(max_length=100)
	ManagerId=models.CharField(max_length=100)
	Department=models.CharField(max_length=100)
	MobileNumber=models.CharField(max_length=10)
	password=models.CharField(max_length=50)
	
	def get_absolute_url(self):
		return reverse('addmanager')

