from account import models
from account import forms

def create_register_form():
    return forms.RegistrationForm()

def create_login_form():
    return forms.LoginForm()

