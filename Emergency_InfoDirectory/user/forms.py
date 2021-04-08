from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from .models import Profile

class SearchForm(forms.Form):       #Homepage_search Form
    CATAGORY_CHOICES= [
        ('','...'),
        ('fire_station', 'Fire Station'),
        ('police', 'Police'),
        ('doctor', 'Doctor'),
        ('hospital', 'Hospital'),
        ('bazar', 'Bazar'),
        ('hotel', 'Hotel'),
        #('divisional_admin', 'Divisional Administration'),     --- thease are Reserved for future uses!
        ('district_admin', 'District Administration'),
        ('subdistrict_admin', 'Subdistrict Administration'),
        #('municipality', 'Municipality'),
        # ('district_council', 'District Council'),
        # ('subdistrict_council', 'Subdistrict Council'),
        ('union', 'Union Council'),
    ]
    DISTRICT_CHOICES= [
        ('','...'),
        ('Kurigram','Kurigram'),
        ('Rangpur', 'Rangpur'),
        ('Dinajpur', 'Dinajpur'),
        ('Lalmonirhat', 'Lalmonirhat'),
        ('Gaibandha', 'Gaibandha'),
        ('Nilphamari', 'Nilphamari'),
        ('Panchagarh', 'Panchagarh'),
    ]
    catagory = forms.CharField(label='Choose a Catagory...', widget=forms.Select(choices=CATAGORY_CHOICES))
    district = forms.CharField(label='Choose a District...', widget=forms.Select(choices=DISTRICT_CHOICES),required=False)

class UserRegistrationForm(UserCreationForm):
    email =forms.EmailField()
    first_name=forms.CharField()
    last_name=forms.CharField()

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  ]

class UserDetailsForm(forms.Form):
    fname = forms.CharField(label='First Name',max_length=15)
    lname = forms.CharField(label='Last Name', max_length=15)
    about = forms.CharField(label='About')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['username',
                'first_name',
                'last_name',
                'email',
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=[
            'profile_picture'
        ]
