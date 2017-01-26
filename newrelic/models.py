from __future__ import unicode_literals

from django.db import models

class api_key(models.Model):
	sitename = models.TextField()
	key = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey('auth.User', related_name='api_key', on_delete=models.CASCADE)

class rest_url(models.Model):
	mode = models.TextField()
	action = models.TextField()
	url = models.TextField()

