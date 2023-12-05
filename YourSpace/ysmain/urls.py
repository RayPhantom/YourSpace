from django.urls import path
from .views import *

urlpatterns = [
	path('', start, name="start"),
	path('signin/', signin, name="signin"),
]