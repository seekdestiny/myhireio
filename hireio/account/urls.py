from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup', views.signup, name='signup'),
    url(r'^signin', views.login, name='signin'),
    url(r'^signout', views.logout, name='signout'),
    url(r'^upload_resume', views.upload_resume, name='upload_resume'),
]
