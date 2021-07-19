from django.db import models
from django.conf import settings

class Admin(models.Model):
    password = models.CharField(max_length=8)

    class Meta:
        db_table = 'admins'