from django.shortcuts import render

# Create your views here.
def HOMEIs(request):
    return render(request,'HOMEIs.html')
def home(request):
    return render(request,'home.html')



