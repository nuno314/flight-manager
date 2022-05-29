from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

from .models import *

# Authentication forms
class LoginForm(AuthenticationForm):
    '''Login form

    Required fields:
        - username
        - password
    '''
    username = forms.CharField(widget = forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your username',
        }
    ))
    password = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your password',
        }
    ))

    class Meta:
        model = User,
        fields = [
            'username',
            'password'
        ]

class RegisterForm(UserCreationForm):
    '''Register form

    Required fields:
        - username (unique)
        - password1
        - password2 (must match with password1)
        - email (valid email)
    '''
    username = forms.CharField(widget = forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your username',
        }
    ))
    email = forms.CharField(widget = forms.EmailInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your email',
        },
    ))
    password1 = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your password',
        },
    ), label = 'Your password')
    password2 = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Confirm your password',
        }
    ), label = 'Confirm your password')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class ChangePasswordForm(PasswordChangeForm):
    '''ChangePasswordForm

    Required fields:
    - old_password
    - new_password1
    - new_password2
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget = forms.PasswordInput(attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your current password'
        })
        self.fields['new_password1'].widget = forms.PasswordInput(attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your new password',
        })
        self.fields['new_password2'].widget = forms.PasswordInput(attrs = {
            'class' : 'form-control',
            'placeholder' : 'Confirm your new password',
        })

class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'

class FlightDetailForm(ModelForm):
    class Meta:
        model = FlightDetail
        fields = '__all__'

class AirportForm(ModelForm):
    class Meta:
        model = Airport
        fields = '__all__'

class CustomerForm(ModelForm):
    '''Customer Form

    Required fields:
    - name
    - phone
    - identity_code
    '''
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = [
            'user',
        ]
    
        widgets = {
            'name' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Your name',
            }),
            'phone' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Your phone',
            }),
            'identity_code' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Your ID',
            }),
        }