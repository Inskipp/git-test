from django.http import HttpResponse
from django.shortcuts import render

def start_page(request):
    # pass
    return render (request, 'main/base.html')
