from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth import logout as django_logout

from .models import *
from .forms import *

# Create your views here.

def start(request):
	context = {
		'title': "Let's start!", 
	} 
	return render(request, 'ysmain/homepages/start.html', context = context)

def signin(request):
	context = {
		'title': "Sign In",
	}
	return render(request, 'ysmain/homepages/signin.html', context = context)