from django.shortcuts import render

# Create your views here.
def my_table(request):

    #sending dynamic data to the html file
    peoples=[{'name':'Anil','age':24},
             {'name':'Omkar','age':13},
             {'name':'Salim','age':22}]
    #'context' is used to send backend data to user 
    context={'user':peoples}
    return render(request,"table.html",context)
