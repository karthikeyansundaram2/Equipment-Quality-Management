from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.core.urlresolvers import reverse
from models import Register,AddEmployee,ChangeAllocation,AddEmployeeDetails
from .models import AddMachine,addmanager
from .models import Login as login
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import AddAMC as AddAMCWarranty
from django.shortcuts import render_to_response



def viewmachinedetails(request):
    machine=AddMachine.objects.all()
    template=loader.get_template('login/viewmachinedetails.html')
    context= {
        'machine' : machine,
          }
    return HttpResponse(template.render(context, request))
    # return render(request, 'personal/index.html' ,context)



def updatemachine(request):
  machine=AddMachine.objects.all()

  context={
    'machine':machine,
  }

  return render(request,'login/updatemachine.html',context)


def viewemployee(request):

  machine=AddMachine.objects.all()
  template=loader.get_template('login/viewemployee.html')
  context= {
    'machine' : machine,
      }
  return HttpResponse(template.render(context, request))


def viewamc(request):
  machine=AddAMCWarranty.objects.all()
  template=loader.get_template('login/viewamc.html')
  context= {
    'machine' : machine,
      }
  return HttpResponse(template.render(context, request))


def updateamcwarranty(request):

  machine=AddAMCWarranty.objects.all()
  template=loader.get_template('login/updateamcwarranty.html')
  context= {
     'machine' : machine,
          }
  return HttpResponse(template.render(context, request))



def deletemachine(request):

  machine=AddMachine.objects.get(id=2)
  machine.delete()
 # mac=AddMachine.objects.all()
  context={
  'machine' : machine,
  #'mac':mac
  }
  #return render(request,'login/viewmachinedetails.html',context)
  return HttpResponse("Ddeleted") 

class LoginCreate(CreateView):
    model = login
    fields = ['Role','LoginId','password']
    



class RegisterCreate(CreateView):
	model = Register
	fields= ['AdminName','AdminID','Department','MobileNumber','password']
	
class AddMachines(CreateView):
	model = AddMachine
	fields= ['MachineName','Manufacturer','Model','SerialNumber','Status','Description','OperatingSystem','EmployeeId','Location','Department','SupportLink','ServiceDate','Specification','PurchasePrice']

class AddAMC(CreateView):
	model = AddAMCWarranty
	fields=['Category','SubCategory','MachineName','Make','Specification','CurrentStatus','PurchaseDate','Vendor','Installationfees']

class AddEmployee(CreateView):
	model = AddEmployee
	fields=['EmployeeId','password']

class ChangeAllocation(CreateView):
	model=ChangeAllocation
	fields=['Category','SubCategory','MachineName','ExistingDepartment','ExistingUser','EarlierAllocationDate','NewDepartment','NewUser','AllocationDate']

def adminpage(request,LoginId,Role):

    
    request.session['LoginId']= LoginId
    request.session['Role']= Role
    

    template=loader.get_template('login/adminpage.html')
    context= {
        
        'LoginId' :request.session['LoginId'],
        'Role' : request.session['Role']
          }
    return HttpResponse(template.render(context, request))

def employee(request,LoginId,Role):
	 
    request.session['LoginId']= LoginId
    request.session['Role']= Role
    

    template=loader.get_template('login/employee.html')
    context= {
        
        'LoginId' :request.session['LoginId'],
        'Role' : request.session['Role']
          }
    return HttpResponse(template.render(context, request))

def manager(request,LoginId,Role):
    if Role == 'manager':
        request.session['LoginId']= LoginId
        request.session['Role']= Role
        template=loader.get_template('login/manager.html')
        context= {
        
          'LoginId' :request.session['LoginId'],
          'Role' : request.session['Role']
          }
        return HttpResponse(template.render(context, request))
    elif Role == 'employee':
        request.session['LoginId']= LoginId
        request.session['Role']= Role  
        template=loader.get_template('login/employee.html')
        context= {
        
          'LoginId' :request.session['LoginId'],
          'Role' : request.session['Role']
          }
        return HttpResponse(template.render(context, request))
    else:
        request.session['LoginId']= LoginId
        request.session['Role']= Role
        template=loader.get_template('login/adminpage.html')
        context= {
        
           'LoginId' :request.session['LoginId'],
           'Role' : request.session['Role']
          }
        return HttpResponse(template.render(context, request))
        
   

        
	 
class AddEmployeeDetails(CreateView):
	model=AddEmployeeDetails
	fields=['EmployeeName','EmployeeId','Department','MobileNumber','password']

class addmanager(CreateView):
	model=addmanager
	fields=['ManagerName','ManagerId','Department','MobileNumber','password']
def logout(request):

  try:
    del request.session['LoginId']
  except:
    pass
  template=loader.get_template('login/register_form.html')
  context= {
        
       #  'LoginId' :request.session['LoginId'],
       #    'Role' : request.session['Role']
    }
  return HttpResponse(template.render(context, request))
      
   
