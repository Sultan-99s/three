from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def page1(request):
    print("page1")
    return HttpResponse('This is page 1.')