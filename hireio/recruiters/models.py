from django.db import models

class AccountInfo(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_engineer = models.BooleanField(default=False)
