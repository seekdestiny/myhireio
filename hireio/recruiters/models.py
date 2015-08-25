from django.db import models

class AccountInfo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    account_id = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_engineer = models.BooleanField(default=False)
