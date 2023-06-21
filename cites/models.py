from typing import Iterable, Optional
from django.db import models

# Create your models here.

class Cite(models.Model):
    owner = models.ForeignKey('users.Member',related_name='cites', on_delete = models.CASCADE, )
    isbn = models.CharField(max_length=13)
    cite = models.CharField(max_length=500)
    autor = models.CharField(max_length=50)
    page = models.IntegerField(default=1)
    dateSave = models.DateField(auto_now=True)