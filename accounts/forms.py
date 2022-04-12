from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [ "email", "password1", "password2"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control '
        self.fields['password1'].widget.attrs['class'] = 'form-control '
        self.fields['password2'].widget.attrs['class'] = 'form-control '

class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    
    