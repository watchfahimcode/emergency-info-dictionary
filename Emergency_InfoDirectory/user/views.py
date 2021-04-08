from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, UserDetailsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user, authenticate, login

@login_required()
def home(request):
    context = {
        'content' : "This is home"
    }
    return render(request,'user/home.html',context)

@login_required
def profile(request):
    if(request.method == 'POST'):
        form=UserDetailsForm(request.POST)
        dict = request.POST
        error_fname = ''
        if dict ['fname']!='' :
            print(dict['fname'])
        else:
            error_fname='First Name is Required!'
            return render(request, 'user/profile.html',
                          { 'form': form,'error_fname':error_fname } )



        print(dict['lname'])
        print(dict['gender'])
        print(dict['division'])

        return redirect('home')

    userDetailsForm = UserDetailsForm()

    return render(request,'user/profile.html',{ 'form': userDetailsForm})

def register(request):
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()

            #autologin...
            username = registration_form.cleaned_data.get('username')
            password = registration_form.cleaned_data.get('password1')
            new_user = authenticate(username=username,password=password)
            login(request,new_user)

        return redirect('home')
    else:
        registration_form = UserRegistrationForm

        context = {

            'form': registration_form
        }
        return render(request, 'user/register.html', context)


