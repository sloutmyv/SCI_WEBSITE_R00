from django.http import HttpResponse
from django.shortcuts import render

# Function based view
def home(request):
    html_="""
    <!doctype html>
    <html lang="en">
    <head>
    </head>
    <body>
    <h1>Hello World !</h1>
    <p>This is html</p>
    </body>
    </html>
    """
    return HttpResponse(html_)
    #return render(request,'home.html',{})
