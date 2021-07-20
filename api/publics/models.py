from django.db import models
from django.db.models.deletion import CASCADE

from api.admins.models import Admin

class Public(models.Model):
    number   = models.CharField(max_length=4)
    password = models.CharField(max_length=4)
    cost     = models.CharField(max_length=10)
    admin    = models.ForeignKey(Admin, on_delete=models.CASCADE)

    class Meta:
        db_table = 'publics'