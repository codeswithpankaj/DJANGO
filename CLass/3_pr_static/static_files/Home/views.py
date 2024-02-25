from django.shortcuts import render
from django.http import HttpResponse

from django.templatetags.static import static

def first(request):
   css_url = static('css/bootstrap.min.css')
   # Do something with the CSS URL

def firstpage(request):
    return render(request,"index.html")

'''
def first(request):

   return HttpResponse("hello andy")
   '''