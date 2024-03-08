from django import forms
from first_app.models import StudentModel


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        # fields = ['roll','name']
        fields = '__all__'
        # exclude = ['address']
        labels = {
            'name' : 'Student Name',
            'roll' : "Student Roll"
        }
        widgets  = {
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name' : "Write your full name"
        }
        
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }