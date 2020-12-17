from django.shortcuts import render

# Create your views here.

def temp(request):
    return render(request,'temp.html')