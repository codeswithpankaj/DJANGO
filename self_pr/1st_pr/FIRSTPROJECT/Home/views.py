from django.shortcuts import render

#self
from django.http import HttpResponse
from Home import views

# Create your views here.
#self
def home(request):
    return HttpResponse("Hey \"Andy\" what's up bro?")