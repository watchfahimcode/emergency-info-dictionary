from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, UserDetailsForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,SearchForm, LocationForm
from django.contrib.auth import get_user, authenticate, login
from .models import Profile
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

#importing data retrieving methods
from bazar.views import showBazarInfo
from Hotel.views import showHotelInfo
from Doctor.views import showDoctorInfo
from Police_station.views import showPoliceStationInfo
from Hospital.views import showHospitalInfo
from fire_station.views import showFireStationInfo
from District_administration.views import showDistrictAdminInfo
from Subdistrict_administration.views import showSubdistrictAdminInfo
from Union_council.views import showUnionCouncilInfo
from user.models import District,Subdistrict,Union

def load_subdistrict(request):                       #_________________Function for AJAX to fetch Subdistricts
    district_id = request.GET.get('district')
    subdistricts = Subdistrict.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'user/subdistrict_list.html', {'subdistricts': subdistricts})


@login_required()   #---Reserved for future use
def home(request):     #home Search Bar
    if request.method == "POST":
        p_form = SearchForm(request.POST)
        q_form = LocationForm(request.POST, instance=request.user)

        if p_form.is_valid():
            dict = request.POST
            catagory = dict['catagory']
            district = District.objects.get(id=dict['district'])
            subdistrict = dict['subdistrict']

            if catagory=='bazar':
                return render(request,'user/result.html',{'results':showBazarInfo(district,subdistrict),'results_name':"Bazar"})   #Bazar Information

            if dict['catagory']=='hotel':
                return render(request,'user/result.html',{'results':showHotelInfo(district,subdistrict),'results_name':"Hotel"})   #Hotel Information

            #Emergency Info
            if dict['catagory']=='doctor':
                return render(request,'user/result.html',{'results':showDoctorInfo(district,subdistrict),'results_name':"Doctor"})  #Doctor Information
            if dict['catagory']=='police':
                return render(request,'user/result.html',{'results':showPoliceStationInfo(district,subdistrict),'results_name':"Police Station"})   #Police Information
            if dict['catagory']=='fire_station':
                return render(request,'user/result.html',{'results':showFireStationInfo(district,subdistrict),'results_name':"Fire Station"})     #Fire Station
            if dict['catagory']=='hospital':
                return render(request,'user/result.html',{'results':showHospitalInfo(district,subdistrict),'results_name':"Hospital"})    #Hospital

            #Admin & Govt. Info
            if dict['catagory']=='district_admin':
                return render(request,'user/result.html',{'results':showDistrictAdminInfo(district),'results_name':"District Administration"})
            if dict['catagory']=='subdistrict_admin':
                return render(request,'user/result.html',{'results':showSubdistrictAdminInfo(district,subdistrict),'results_name':"Subdistrict Administration"})
            #.....update result page
            # if dict['catagory']=='municipality':
            #     return render(request,'user/result.html',{'results':showMunicipalityInfo(district,subdistrict),'results_name':"Municipality"})
            if dict['catagory']=='union':
                return render(request,'user/result.html',{'results':showUnionCouncilInfo(district,subdistrict),'results_name':"Union"})


    else:
        p_form = SearchForm
        q_form = LocationForm
        return render(request, 'user/home.html',{'search_forms':p_form, 'location_forms':q_form})

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

            # sending welcoming  mail
            subject = 'welcome to our project'
            body = render_to_string('user/intro_email.html')
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [new_user.email]
            )




        #sending welcoming  mail
        subject='welcome to our project'
        body=render_to_string('user/intro_email.html')
        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [new_user.email]

        )
        #extra line added
        return redirect('home')


    else:
        registration_form = UserRegistrationForm

        context = {
            'form': registration_form
        }
        return render(request, 'user/register.html', context)



