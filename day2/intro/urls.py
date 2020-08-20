from django.contrib import admin
from django.http import HttpResponse
from django.conf.urls import include, url
import operator
from intro import views
urlpatterns = [
	url(r'aboutus.*', views.aboutus, name = 'aboutus'),
	url(r'hobbies.*', views.hobbies, name = 'hobbies'),
]
