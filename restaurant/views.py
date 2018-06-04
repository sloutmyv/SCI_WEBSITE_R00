import random
from django.http import HttpResponse
from django.shortcuts import render

from django.views import View

# Function based view
def home(request):
    num = random.randint(0,1000)
    some_list = [num, random.randint(0,1000),random.randint(0,1000)]
    context = {
        'bool_item':False,
        'num': num,
        'some_list':some_list}

    return render(request,'home.html',context)

def about(request):
    context = {}
    return render(request,'about.html',context)

def contact(request):
    context = {}
    return render(request,'contact.html',context)

class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request,'contact.html',context)
