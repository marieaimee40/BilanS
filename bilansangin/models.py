import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator
# Create your models here.

class MonitoredTimeModel(models.Model):
	creation_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class Enregistrement(MonitoredTimeModel):
    genre = models.CharField(max_length=3,blank=False, verbose_name="Genre du patient")
    code=models.CharField(max_length=30,blank=False)
    date_prelevement = models.DateField("Date du prélèvement",null=True)
    date_traitement = models.DateField(null=True)
    copies_ARN = models.CharField(max_length=20,blank=False, verbose_name="nombre de copies ARN")
    log_copies_ARN = models.CharField(max_length=20,blank=False, verbose_name="Log ARN")
