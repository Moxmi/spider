from django.db import models

# Create your models here.
class AddLogpath(models.Model):
	logpath = models.CharField(max_length=500)
