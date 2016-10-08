from django import forms


class StudentForm(forms.Form):
    student_id = forms.CharField(max_length=100, label="Student Id")
    first_name = forms.CharField(max_length=100,  label="First Name")
    last_name = forms.CharField(max_length=100,  label="Last Name")
    email = forms.CharField(max_length=100,  label="E-mail")
    address = forms.CharField(max_length=100,  label="Address")
    gpa = forms.DecimalField(min_value=0, max_value=4.0)