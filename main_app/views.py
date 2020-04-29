from django.shortcuts import render
from .models import Cat

# class Cat(models.Model):
#   name = models.CharField(max_length=100)
#   breed = models.CharField(max_length=100)
#   description = models.TextField(max_length=250)
#   age = models.IntegerField()

# def __str__(self):
#   return self.name

# cats = [
#   Cat('Lolo', 'Tabby', 'foul little demon', 3),
#   Cat('Sachi', 'Tortoise Shell', 'Diluted Tortoise Shell', 0),
#   Cat('Raven', 'Black Tripod', '3 legged cat', 4)
# ]

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', { 'cat': cat })
