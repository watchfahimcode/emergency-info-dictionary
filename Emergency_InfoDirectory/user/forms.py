from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from .models import Profile

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

class UserUpdateForm(forms.ModelForm):
    username=forms.CharField(max_length=25,required=False)
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',

        ]
class ProfileUpdateForm(forms.ModelForm):
    profile_picture=forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = [

            'profile_picture'
        ]
