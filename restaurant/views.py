from django.http import HttpResponse
from django.shortcuts import render

# Function based view
def home(request):
    return HttpResponse("Hello")
    #return render(request,'home.html',{})
