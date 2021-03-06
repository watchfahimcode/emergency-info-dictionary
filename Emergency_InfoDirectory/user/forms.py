from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from .models import Profile
from .models import Subdistrict
from .models import District
from .models import Union


class LocationForm(forms.ModelForm):          #Homepage_search Form
    class Meta:
        model = Union
        fields = ('district', 'subdistrict')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subdistrict'].queryset = Subdistrict.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['subdistrict'].queryset = Subdistrict.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['subdistrict'].queryset = self.instance.district.subdistrict_set.order_by('name')



class SearchForm(forms.Form):       #Homepage_search Form
    CATAGORY_CHOICES= [
        ('','---------'),
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
        ('','---------'),
        ('Kurigram','Kurigram'),
        ('Rangpur', 'Rangpur'),
        ('Dinajpur', 'Dinajpur'),
        ('Lalmonirhat', 'Lalmonirhat'),
        ('Gaibandha', 'Gaibandha'),
        ('Nilphamari', 'Nilphamari'),
        ('Panchagarh', 'Panchagarh'),
    ]
    catagory = forms.CharField(label='Choose a Catagory...', widget=forms.Select(choices=CATAGORY_CHOICES))
    #district = forms.CharField(label='Choose a District...', widget=forms.Select(choices=DISTRICT_CHOICES),required=False)

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
    username = forms.CharField(max_length=20, required=False)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.CharField(max_length=30, required=False)
    class Meta:
        model= User
        fields=['username',
                'first_name',
                'last_name',
                'email',
        ]


class ProfileUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields=[
            'profile_picture'
        ]
