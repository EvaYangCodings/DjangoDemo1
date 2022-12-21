from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    favorite_book = {'Raymond':"Book1", 'Emma': 'book2'}
    return render(request, 'first_app/index.html', context=favorite_book)
def home(request):
    return HttpResponse("Welcome to the home page!")
def educative(request):
    return HttpResponse("Welcome to the educative page!")
# def show_age(request, age):
#     return HttpResponse("I am %s years old." % age)
def even_or_odd(request, num):
    if(num % 2 == 0):
        output = "%s is an even number." % num
    else:
        output = "%s is an odd number." % num
    return HttpResponse(output)