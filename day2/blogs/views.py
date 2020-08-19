from django.shortcuts import render
import operator
from django.http import HttpResponse
# Create your views here.
def drinks(requests):
	return HttpResponse('Water is a great saviour at times.')
def foods(requests):
	return HttpResponse('Food is essential for the survivial of animals.')


