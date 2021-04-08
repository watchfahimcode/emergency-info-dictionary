from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User

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