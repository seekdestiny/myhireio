from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render

from account import forms
from account import models

def recruiter_register(request):
    if request.method == 'GET':
        return show_registration_page(request)
    elif request.method == 'POST':
# TODO need to use https
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.data.get('username'),
                form.data.get('email'),
                form.data.get('password'),
            )
            user.save()

            return render(
                request,
                'desktop/landing_pages/index.html',
            )
        else:
            return show_registration_page(request)

def show_registration_page(request):
    template = 'desktop/account/recruiter_register.html'
    form = forms.RegistrationForm()
    return render(
        request,
        template,
        {
            'form': form,
        },
    )

def login(request):
    if request.method == 'GET':
        return show_login_page(request)
    elif request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if not form.is_valid():
            return show_login_page(request)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is None:
            return show_login_page(request)

        auth.login(request, user)
        return render(
            request,
            'desktop/landing_pages/index.html',
        )


def show_login_page(request):
    template = 'desktop/account/login.html'
    form = forms.LoginForm()
    return render(
        request,
        template,
        {
            'form': form,
        },
    )

def upload_resume(request):
    if request.method == 'POST':
        form = forms.UploadResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = models.Resume(
                resume=request.FILES['resume'],
                title=form.cleaned_data.get('title'),
                user=request.user,
            )
            resume.save()

            return render(
                request,
                'desktop/landing_pages/index.html',
            )
        else:
            return render(
            request,
            'desktop/account/upload_resume.html',
            {
                'form': form,
            }
        )
    else:
        form = forms.UploadResumeForm()
        return render(
            request,
            'desktop/account/upload_resume.html',
            {
                'form': form,
            }
        )
