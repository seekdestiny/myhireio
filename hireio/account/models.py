from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='resumes/')

class Profile(models.Model):
    user = models.OneToOneField(User)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile, created = Profile.objects.get_or_create(user=instance)

    post_save.connect(create_user_profile, sender=User)

class Resume(models.Model):
    user = models.ForeignKey(User)

    title = models.CharField(max_length=100, blank=False)
    resume = models.FileField(storage=fs)

