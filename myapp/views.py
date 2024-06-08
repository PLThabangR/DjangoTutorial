from django.shortcuts import render

from django.http import HttpResponse 

#The view function reads the path, query, and body parameters included in the client's request If required, 
# it uses this data to interact with the models to perform CRUD operations.
def home(request): 
    return HttpResponse("Hello, world. This is the.") 
# Create your views here.
