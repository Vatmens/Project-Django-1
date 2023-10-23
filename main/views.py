from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
        'title': 'Main page',
        'values': ['Some', 'Hello', 'Main frau'],
        'obj': {
            'car': "BNW",
            'age': 9,
            'hobby': 'football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')