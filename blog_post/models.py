from django.db import models
from django.contrib.auth.models import User
from django.utils import tree
from taggit.managers import TaggableManager
from user.models import Guest


class Blog(models.Model):
	blog_image = models.ImageField(upload_to='images/blog_images')
	blog_heading = models.CharField(max_length=100, null=True)
	blog_text = models.CharField(max_length=255, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name="blog_posts")

	tags = TaggableManager()


	def total_likes(self):
		return self.likes.count()


	def __str__(self):
		return self.blog_heading

 
class BlogComment(models.Model):
	message = models.CharField(max_length=255, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')
	guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True)
	active = models.BooleanField(default=True)
	

	def __str__(self):
		return self.message


