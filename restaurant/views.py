import random
from django.http import HttpResponse
from django.shortcuts import render

# Function based view
def home(request):
    num = random.randint(0,1000)
    return render(request,'base.html',{'var':'Context variable', 'num': num})
