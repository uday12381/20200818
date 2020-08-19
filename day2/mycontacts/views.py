from django.shortcuts import render
import operator
from django.http import HttpResponse
# Create your views here.
def contactslist(requests):
	return HttpResponse('Your contact list is empty as of now')
def friends(requests):
	return HttpResponse('Your friends list is empty as of now')
	
