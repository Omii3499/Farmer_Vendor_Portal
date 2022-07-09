import imp
from django.forms import ModelForm
from myapp.models import Reg
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(ModelForm):
    class Meta:
        model=Reg
        # fields= '__all__'
        fields=['First Name', 'Last Name', 'Date Of Birth', 'Gender', 'Address', 'City', 'State', 'PINCODE', 'Mobile_number']

form = RegisterForm() 


