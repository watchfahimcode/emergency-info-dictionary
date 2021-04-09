from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, UserDetailsForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,SearchForm
from django.contrib.auth import get_user, authenticate, login
from .models import Profile

#importing data retrieving methods
from bazar.views import showBazarInfo
from Hotel.views import showHotelInfo
from Doctor.views import showDoctorInfo
from Police_station.views import showPoliceStationInfo
from Hospital.views import showHospitalInfo
from fire_station.views import showFireStationInfo
from District_administration.views import showDistrictAdminInfo
from Subdistrict_administration.views import showSubdistrictAdminInfo
from Municipality.views import showMunicipalityInfo
from Union_council.views import showUnionCouncilInfo

@login_required()   #---Reserved for future use
def home(request):     #home Search Bar
    if request.method == "POST":
        q_form = SearchForm(request.POST)
        if q_form.is_valid():
            dict = request.POST

            if dict['catagory']=='bazar':
                return render(request,'user/result.html',{'results':showBazarInfo(dict['district']),'results_name':"Bazar"})   #Bazar Information
            if dict['catagory']=='hotel':
                return render(request,'user/result.html',{'results':showHotelInfo(dict['district']),'results_name':"Hotel"})   #Hotel Information

            #Emergency Info
            if dict['catagory']=='doctor':
                return render(request,'user/result.html',{'results':showDoctorInfo(dict['district']),'results_name':"Doctor"})  #Doctor Information
            if dict['catagory']=='police':
                return render(request,'user/result.html',{'results':showPoliceStationInfo(dict['district']),'results_name':"Police Station"})   #Police Information
            if dict['catagory']=='fire_station':
                return render(request,'user/result.html',{'results':showFireStationInfo(dict['district']),'results_name':"Fire Station"})     #Fire Station
            if dict['catagory']=='hospital':
                return render(request,'user/result.html',{'results':showHospitalInfo(dict['district']),'results_name':"Hospital"})    #Hospital

            #Admin & Govt. Info
            if dict['catagory']=='district_admin':
                return render(request,'user/result.html',{'results':showDistrictAdminInfo(dict['district']),'results_name':"District Administration"})
            if dict['catagory']=='subdistrict_admin':
                return render(request,'user/result.html',{'results':showSubdistrictAdminInfo(dict['district']),'results_name':"Subdistrict Administration"})
            #.....update result page
            if dict['catagory']=='municipality':
                return render(request,'user/result.html',{'results':showMunicipalityInfo(dict['district']),'results_name':"Municipality"})
            if dict['catagory']=='union':
                return render(request,'user/result.html',{'results':showUnionCouncilInfo(dict['district']),'results_name':"Union"})


    else:
        q_form = SearchForm
        return render(request, 'user/home.html',{'search_forms':q_form})

def about(request):        #about Page
    return render(request,'user/about.html')

def contact(request):        #contact Page
    return render(request,'user/contact_us.html')

@login_required()
def result(request):        #result Page
    return render(request,'user/result.html')

@login_required()
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


@login_required()
def profile_update(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance= request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES,
                                               instance=request.user.profile)

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
        user_update_form = UserUpdateForm(instance= request.user)
        profile_update_form = ProfileUpdateForm()
        context = {
            'user_update_form' : user_update_form,
            'profile_update_form': profile_update_form

        }
        return render(request,'user/profile_update.html',context)


def register(request):
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            #profile = Profile(user=request.user)  #alteranate
            #profile.save

            #autologin...
            username = registration_form.cleaned_data.get('username')
            password = registration_form.cleaned_data.get('password1')
            new_user = authenticate(username=username,password=password)
            login(request,new_user)

        return redirect('home')

        #else:
            #return redirect('home')


    else:
        registration_form = UserRegistrationForm

        context = {
            'form': registration_form
        }
        return render(request, 'user/register.html', context)


