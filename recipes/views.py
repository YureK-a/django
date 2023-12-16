from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home (request):
  return HttpResponse(render(request, 'recipes/pages/home.html', context={
    'name': 'Yure'
	}))

def recipe (request, id):
  return HttpResponse(render(request, 'recipes/pages/recipe-view.html', context={
    'name': 'Yure'
	}))