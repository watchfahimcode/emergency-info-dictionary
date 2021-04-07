from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from .models import Profile
def profile(request):
    context = {
        # 'name' : "Fahim",
        # 'email' : "fahimrahman@uap.gmail.com",
    }
    return render(request,'user/profile.html',context)

def register(request):
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            # profile = Profile(user=request.user)
            # profile.save()
            return redirect('user-profile')


    else:
        registration_form = UserRegistrationForm

        context = {

            'form': registration_form
        }
        return render(request, 'user/register.html', context)

@login_required
def profile_update(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST,instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            return redirect('user-profile')
        else:
            context = {
                    'user_update_form': user_update_form,
                    'profile_update_form': profile_update_form
            }
            return render(request, 'user/profile_update.html', context)

    else:
            user_update_form=UserUpdateForm(instance=request.user)
            profile_update_form=ProfileUpdateForm()
            context={
            'user_update_form' : user_update_form,
            'profile_update_form': profile_update_form
                 }

            return render(request,'user/profile_update.html',context)
