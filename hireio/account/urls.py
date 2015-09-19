from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recruiter_register', views.recruiter_register, name='recruiter_register'),
    url(r'^login', views.login, name='login'),
    url(r'^upload_resume', views.upload_resume, name='upload_resume'),
]