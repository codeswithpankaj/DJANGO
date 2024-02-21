from django.shortcuts import render

#self
from django.http import HttpResponse


# Create your views here.
#self
def home(request):
   return HttpResponse("Hey \"Andy\" what's up bro?")