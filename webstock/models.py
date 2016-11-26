from __future__ import unicode_literals

from django.db import models

# Create your models here.

class stocks(models.Model):
	symbol = models.CharField(max_length = 10)
	date = models.DateField()
	opening = models.FloatField()
	closing = models.FloatField()

	def __str__(self):
		return '%s on %s' % (self.symbol, self.date)