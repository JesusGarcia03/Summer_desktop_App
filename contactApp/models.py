from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Record(models.Model):
	create_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	#bio = models.CharField(max_length=100)
	#email = models.EmailField(maxlength=30)
	email = models.CharField(max_length=30)
	phone = models.CharField(max_length=10)


	def __str__(self):
		return(f"{self.first_name}{self.last_name}")
	
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=10)

	def __str__(self):
		return self.user.username
	
class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return f"{self.author.username} posted at {self.created_at}"

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.author.username} commented on {self.post.id}"
	
