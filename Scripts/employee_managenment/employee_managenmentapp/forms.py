from django import forms
from .models import Employee, Department, EmployeeSalary

# class StudentRegistration(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['name','email','password']
#         widgets={
#             'name':forms.TextInput(attrs={'class':"form-control"}),
#             'email':forms.EmailInput(attrs={'class':"form-control"}),
#             'password':forms.PasswordInput(render_value=True,attrs={'class':"form-control",})
#         }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSalaryForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = '__all__'



class SalaryReportForm(forms.Form):
    start_date = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type': 'date'}))
