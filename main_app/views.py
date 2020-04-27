from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Cat:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

cats = [
  Cat('Lolo', 'Tabby', 'foul little demon', 3),
  Cat('Sachi', 'Tortoise Shell', 'Diluted Tortoise Shell', 0),
  Cat('Raven', 'Black Tripod', '3 legged cat', 4)
]

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  return render(request, 'cats/index.html', {
		'cats': cats
	})


