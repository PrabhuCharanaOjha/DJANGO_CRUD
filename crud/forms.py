from django import forms
from .models import Student


class Studentdata(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id', 'stu_roll', 'stu_name',
                  'stu_email', 'stu_mobile', 'stu_image']
        labels = {'stu_roll': 'Roll Number', 'stu_name': 'Name',
                  'stu_email': 'Email', 'stu_mobile': 'Mobile Number', 'stu_image': 'Profile Picture'}
        widgets = {
            'stu_roll': forms.NumberInput(attrs={"class": "form-control my-1", "placeholder": "please enter roll number"}),
            'stu_name': forms.TextInput(attrs={"class": "form-control my-1", "placeholder": "please enter student name"}),
            'stu_email': forms.EmailInput(attrs={"class": "form-control my-1", "placeholder": "please enter student email"}),
            'stu_mobile': forms.NumberInput(attrs={"class": "form-control my-1", "placeholder": "please enter student mobile number"}),
            'stu_image': forms.ClearableFileInput(attrs={"class": "form-control my-1"}),
        }
