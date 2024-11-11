from django.shortcuts import render

from django.http import HttpResponse


def home(request):

    peoples = [
    {'name': 'John', 'age': 45},
    {'name': 'Jane', 'age': 20},
    {'name': 'Jim', 'age': 10},
    {'name': 'Jill', 'age': 25},
    {'name': 'Jack', 'age': 50},
]
    varsity = [
        'University of North Dakota', 'Michigan University', 'University of California', 'University of Texas', 'University of Florida'
    ]
    return render(request, 'home/index.html', context={'peoples': peoples, 'varsity': varsity})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def page1(request):
    print("page1")
    return HttpResponse('This is page 1.')