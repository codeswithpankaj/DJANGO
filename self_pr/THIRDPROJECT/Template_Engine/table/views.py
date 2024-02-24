from django.shortcuts import render

# Create your views here.
def my_table(request):
    return render(request,"table.html")
