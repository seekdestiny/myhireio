from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

def register(request):
    if request.method == 'GET':
        template = loader.get_template('recruiters/register.html')
        return HttpResponse(template.render())
    elif request.method == 'POST':
        None
