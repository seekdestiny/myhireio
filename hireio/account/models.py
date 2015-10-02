from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='resumes/')

class Talent(models.Model):
    user = models.OneToOneField(User)

    def create_talent(sender, instance, created, **kwargs):
        if created:
            talent, created = Talent.objects.get_or_create(user=instance)

    post_save.connect(create_talent, sender=User)

class Recruiter(models.Model):
    user = models.OneToOneField(User)

    def create_recruiter(sender, instance, created, **kwargs):
        if created:
            recruiter, created = Recruiter.objects.get_or_create(user=instance)

    post_save.connect(create_recruiter, sender=User)

class Resume(models.Model):
    user = models.ForeignKey(User)

    title = models.CharField(max_length=100, blank=False)
    resume = models.FileField(storage=fs)

