from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserAdminCreationForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('Email')
            messages.success(request,f'Your account has been created.Logon now')
            return redirect('login')
    else:
        form=UserAdminCreationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')