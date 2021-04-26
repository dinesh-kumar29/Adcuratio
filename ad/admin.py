from django.contrib import admin
from .models import Employee
from .models import User

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age','gender','email','phoneNo')
admin.site.register(Employee, EmployeeAdmin)



