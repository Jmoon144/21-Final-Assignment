from django.db import models
from django.db.models.deletion import CASCADE

class Public(models.Model):
    number   = models.CharField(max_length=4)
    password = models.CharField(max_length=4)
    cost     = models.CharField(max_length=10)

    class Meta:
        db_table = 'publics'