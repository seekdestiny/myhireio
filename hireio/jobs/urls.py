from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create_job', views.create_job, name='create_job'),
    url(r'^create_company', views.create_company, name='create_company'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^load_more_companies', views.load_more_companies, name='load_more_companies'),
    url(r'^job_detail', views.job_detail, name='detail'),
]