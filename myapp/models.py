from django.db import models

# Create your models here.
class LongToShort(models.Model):
	long_url = models.URLField(max_length = 500)
	short_url = models.CharField(max_length = 50, unique = True)
	date = models.DateField(auto_now_add = True)
	clicks = models.IntegerField(default = 0)
	country_clicks = models.JSONField(default = dict, blank = True)
	desktop_clicks = models.IntegerField(default = 0)
	mobile_clicks = models.IntegerField(default = 0)
	last_country = models.CharField(max_length = 100, default = "Unknown")
	last_device = models.CharField(max_length = 20, default = "Desktop")
	last_clicked_at = models.DateTimeField(null = True, blank = True)

	def __str__(self):
		return self.short_url
