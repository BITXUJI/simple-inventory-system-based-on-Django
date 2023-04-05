from django import forms
from django.forms import DateInput
from .models import Item
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'quantity', 'expiration_date', 'description']
        widgets = {
            'expiration_date': DateInput(attrs={'type': 'date'}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))