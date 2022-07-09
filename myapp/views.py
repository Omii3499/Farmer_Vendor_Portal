from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Reg


# Create your views here.

def home(request):
    return render(request, 'Home/home.html')

# def home(request):
#     return render(request, 'test.html')    

def register(request):
    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
        else:
           return form    

    else:
        form=RegisterForm()
   
    return render(request,'Register/register.html', {'form':form})

