from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   people = [
      {"name": "Alice Johnson","age": 28,"phone": "+1-555-0147"},
      {"name": "Bob Smith","age": 34,"phone": "+1-555-0198"},
      {"name": "Charlie Davis","age": 22,"phone": "+1-555-0123"},
      {"name": "Bob Smith","age": 34,"phone": "+1-555-0198"},
      {"name": "Bob Smith","age": 34,"phone": "+1-555-0198"},
   ]
   # return HttpResponse("Hello, world. You're at the first index.")
   context = {
      "title": "INDEXXXX",
      "heading":"Index",
      "para": "Welcome to the index page",
      "people": people
   }
   return render(request, 'index.html', context)

def home(request):
   context = {
      "title": "Home Page",
      "heading":"Home Page",
      "para": "Welcome to the home page"
   }
   return render(request, 'home.html', context)

# contact us, about us, home function and urls define, template(html)