from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from mycontacts import views
urlpatterns = [
	url(r'contactslist.*', views.contactslist, name = 'contactslist'),
	url(r'friends.*', views.friends, name = 'friends'),
]
