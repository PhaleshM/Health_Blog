from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    name = forms.CharField(max_length=150, required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    term_and_condition = forms.BooleanField(required=True)
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ('email', 'name', 'phone_number', 'term_and_condition', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            return email.lower()
        else:
            raise ValidationError("Email field cannot be empty.")



class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Emaillll',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


