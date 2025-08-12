from django.db import models

# Create your models here.
class Record(models.Model):
	create_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	#email = models.EmailField(maxlength=30)
	email = models.CharField(max_length=30)
	phone = models.CharField(max_length=10)


	def _str_(self):
		return(f"{slef.first_name}{self.last_name}")