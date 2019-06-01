from django.contrib import admin

from .models import Login , Register , AddEmployee,AddMachine,ChangeAllocation,AddAMC

admin.site.register(Login)
admin.site.register(Register)
admin.site.register(AddMachine)
admin.site.register(AddEmployee)
admin.site.register(ChangeAllocation)
admin.site.register(AddAMC)