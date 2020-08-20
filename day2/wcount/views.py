from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def home(requests):
	return render(requests, 'wcount/home.html')

def count(requests):
	text = requests.GET["textarea1"]
	wcount = len(text.split())
	return render(requests, 'wcount/count.html', {'wcount' : wcount})

