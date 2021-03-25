from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

def profile(request):
    context =  {
        'name' : "Fahim",
        'email' : "fahimrahman@uap.gmail.com",
    }
    return render(request,'user/profile.html',context)

def register(request):
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('user-profile')
    else:
        registration_form = UserRegistrationForm

        context = {

            'form': registration_form
        }
        return render(request, 'user/register.html', context)


