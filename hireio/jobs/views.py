from forms import CompanyForm, JobPostForm
from django.shortcuts import render
from models import Company, JobPost
from datetime import datetime
from django.core.serializers import serialize
from django.http import JsonResponse
import json
from django.http import HttpResponse

def create_job(request):
    template = 'jobs/new_job.html'
    if request.method == 'GET':
        template = 'jobs/new_job.html'
        form = JobPostForm()
        return render(
            request,
            template,
            {
                'form': form
            }
        )
    elif request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            company = Company.objects.get(name=form.cleaned_data.get('company'))
            job_post = JobPost(
                description = form.cleaned_data.get('description'),
                requirements = form.cleaned_data.get('requirements'),
                skills = form.cleaned_data.get('skills'),
                location = form.cleaned_data.get('location'),
                salary = form.cleaned_data.get('salary'),
                equity = form.cleaned_data.get('equity'),
                job_type = form.cleaned_data.get('job_type'),
                job_title = form.cleaned_data.get('job_title'),
                responsibility = form.cleaned_data.get('responsibility'),
                company = company,
            )
            job_post.save()
            return render(
                request,
                'landing_pages/index.html',
            )
        else:
            return render(
                request,
                template,
                {
                    'form': form
                }
            )

def job_detail(request):
    if request.method == 'GET':
        template = 'jobs/job_detail.html'
        job_id = int(request.GET.get('job_id', ''))
        if not job_id:
            job_post = None
        else:
            job_post = JobPost.objects.get(id=job_id).serialize()
        return HttpResponse(json.dumps(job_post), content_type="application/json")

def create_company(request):
    if request.method == 'GET':
        template = 'jobs/new_company.html'
        form = CompanyForm()
        return render(
            request,
            template,
            {
                'form': form
            }
        )
    elif request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = Company(
                name = form.cleaned_data.get('name'),
                tag_name = form.cleaned_data.get('tag_name'),
                product = form.cleaned_data.get('product'),
                why_us = form.cleaned_data.get('why_us'),
                traction = form.cleaned_data.get('traction'),
                funding = form.cleaned_data.get('funding'),
                size = form.cleaned_data.get('size'),
                last_active = datetime.now(),
                market = form.cleaned_data.get('market'),
                company_link = form.cleaned_data.get('company_link'),
            )
            company.save()

            return render(
                request,
                'landing_pages/index.html',
            )

def dashboard(request):
    if request.method == 'GET':
        template = 'jobs/dashboard.html'

        return render(
            request,
            template,
        )

def load_more_companies(request):
    company_models = Company.objects.order_by('last_active')

    start = int(request.GET.get('index', 0))
    end = start + 10
    if end > company_models.count():
        end = company_models.count()
    last_ten_companies = company_models[start:end]

    companies = []
    for company in last_ten_companies:
        serialized_item = company.serialize()
        serialized_item['jobs'] = []

        for jobpost in company.jobpost_set.all():
            serialized_item['jobs'].append(jobpost.serialize())

        companies.append(serialized_item)

    return HttpResponse(json.dumps(companies), content_type="application/json")
