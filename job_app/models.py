from django.db import models


class Job(models.Model):
	title = models.CharField(max_length=64)
	salary = models.IntegerField()
	address = models.CharField(max_length=128, default="None")
	lat = models.FloatField()
	lon = models.FloatField()
	
	def __str__(self):
		return self.title