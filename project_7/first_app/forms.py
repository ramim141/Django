from django import forms
from first_app.models import StudentModel


class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentModel
        # fields = ("",)
        fields = "__all__"
        # feild = ['name', 'rollno', 'city']
        # exclude = ['father_name']
        labels = {
            "father_name": "Father Name",
            "address": "Address"
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": 'btn-primary', "placeholder": "Enter Your Name"}),
            "rollno": forms.TextInput(attrs={"class": "input", "placeholder": "Enter Your Roll No"}),
        }
        
        help_texts = {
            "father_name": "Enter Your Father Name",
        }
        
        error_messages = {
            "father_name": {"required": "Please Enter Your Father Name"}
        }
