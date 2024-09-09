from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget= forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    class Meta:
       model = User
       fields = (
           'first_name',
           'last_name',
           'email',
           'username',
           'password1',
           'password2',
           
       )
       def __init__(self, *args, **kwargs):
           super(RegisterForm, self).__init__(*args, **kwargs)
           self.fields['username'].widget.attrs['class'] = 'form-control'
           self.fields['password1'].widget.attrs['class'] = 'form-control'
           self.fields['password2'].widget.attrs['class'] = 'form-control'
     
class   LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class' : 'form-control'
            }
        )
    )
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    