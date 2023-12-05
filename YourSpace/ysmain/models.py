from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class Info(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True)
	content= models.TextField()
	is_pub = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('info_focus', kwargs={'slug': self.slug})

class User(AbstractUser):
    slug = models.SlugField(unique=True)
    descr = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    cover_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")