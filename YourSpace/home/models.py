from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

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

    """def __str__(self):
    	return str(self.user)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})"""


# ИСПРАВИТЬ ОШИБКУ И СДЕЛАТЬ МИГРАЦИЮ!!!

def user_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class ProfileContent(models.Model):
	profile = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	conttype = models.ForeignKey('ContentType', null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name

class ContentType(models.Model):
	typename = models.CharField(max_length=255)

	def __str__(self):
		return self.typename

class TextContent(models.Model):
	name = models.CharField(max_length=255)
	content = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name

class ImgContent(models.Model):
	name = models.CharField(max_length=255)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	content = models.ImageField(null=True, blank=True, upload_to=user_directory_path)

	def __str__(self):
		return self.name
