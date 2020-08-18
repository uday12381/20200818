from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.

def home(requests):
	return HttpResponse('<h1>Welcome to the home page</h1>')

def aboutus(requests):
	return HttpResponse('<h1>J Uday Reddy, 3rd year, Information Technology, Vasavi College of Engineering</h1>')

def hobbies(request):
	return HttpResponse('<h1>Hobbies: Touch typing, Solving Sudoku puzzles, Problem solving using programming</h1>')

