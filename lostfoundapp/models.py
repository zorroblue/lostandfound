from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Notice(models.Model):
	notice_id = models.AutoField(primary_key = True)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	user_id = models.CharField(max_length=20)
	image_url = models.CharField(max_length=200, default ="http://placehold.it/350x150")


