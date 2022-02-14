from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'name': 'Phizy',
        'age': '14',
        'nickname': 'Sharky',
    }
    return render(request, 'index.html', context)
