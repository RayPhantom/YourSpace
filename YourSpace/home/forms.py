from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.contrib.auth import get_user_model
User = get_user_model()

#ДОБАВИТЬ КАПЧУ https://django-simple-captcha.readthedocs.io/en/latest/usage.html#installation

class signupform(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': "logcon name", 'autocomplete': "off"}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "logcon", 'autocomplete': "off"}))
	password1= forms.CharField(widget=forms.PasswordInput(attrs={'class': "logcon"}))
	password2= forms.CharField(widget=forms.PasswordInput(attrs={'class': "logcon"}))

	#captcha = CaptchaField()

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2',)

class signinform(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': "logcon", 'autocomplete': "off"}))
	password= forms.CharField(widget=forms.PasswordInput(attrs={'class': "logcon"}))
	#captcha = CaptchaField()

class AddText(forms.ModelForm):
	name = forms.CharField(widget=forms.HiddenInput(attrs={'class': "TextField", 'value': "name"}))
	content = forms.CharField(widget=forms.TextInput(attrs={'class': "TextField", 'autocomplete': "off"}), label="")

	class Meta:
		model = TextContent
		fields = ('name', 'content',)

class AddImg(forms.ModelForm):
	name = forms.CharField(widget=forms.HiddenInput(attrs={'class': "TextField", 'value': "name"}))
	content = forms.ImageField(widget=forms.FileInput(attrs={'class': "ImgField"}), label="")
	class Meta:
		model = ImgContent
		fields = ('name', 'content',)

class ProfileEditForm(forms.Form):
	descr = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': "TextField", 'value': "Description"}), label="Описание профиля")
	profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': "ImgField", 'value': "images/profile/defava.png"}),required=False, label="Фото профиля")
	cover_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': "ImgField", 'value': "images/profile/defcover.png"}),required=False, label="Фон профиля")