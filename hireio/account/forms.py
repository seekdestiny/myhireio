import re

from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.EmailField(label='Account Id (your email address)', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        previous = User.objects.filter(username=username)
        if len(previous):
            raise forms.ValidationError('This email has already been used.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        return password

class LoginForm(forms.Form):
    def is_valid(self):
        valid = super(LoginForm, self).is_valid()
        username = self.cleaned_data.get('username')
        user = User.objects.get(username=username)
        if not user:
            valid = False
        return valid

    username = forms.EmailField(
        label = 'Account Id (your email address)',
        widget = forms.TextInput(
            attrs = {'autofocus': 'true'}
        )
    )

    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(
            attrs = {}
        ),
    )

class UploadResumeForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    resume = forms.FileField()
