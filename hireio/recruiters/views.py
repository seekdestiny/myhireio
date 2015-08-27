from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from recruiters.models import AccountInfo

from recruiters import forms

def register(request):
    if request.method == 'GET':
        return show_registration_page(request)
    elif request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            AccountInfo.objects.create(
                user_name = form.data.get('username'),
                email = form.data.get('email'),
# TODO need to encrypt it
# TODO need to use https
                password = form.data.get('password'),
            )
            return render(
                request,
                'landing_pages/index.html',
            )
        else:
            return show_registration_page(request)

def show_registration_page(request):
    template = 'recruiters/register.html'
    form = forms.RegistrationForm()
    return render(
        request,
        template,
        {
            'form': form,
        },
    )

