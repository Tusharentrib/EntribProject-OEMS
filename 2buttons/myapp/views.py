#from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world!")

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def formtable(request):
    return render(request, 'formtable.html')
