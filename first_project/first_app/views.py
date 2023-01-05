from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm, TestForm, PostModelForm
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.
# def index(request):
#     # favorite_book = {'Raymond':"Book1", 'Emma': 'book2'}
#     # return render(request, 'first_app/index.html', context=favorite_book)
#     # tv_shows_list={"tv_shows":{'Game of Thrones':'9.3','Blacklist': '8','Suits': '8.5','The Witcher': '8.5'}}
#     # return render(request, 'first_app/index.html', context=tv_shows_list)
#     filters = {"value" : "We are learning filters."}
#     return render(request, 'first_app/index.html', context=filters)

def home(request):
    # return HttpResponse("Welcome to the home page!")
    # return render(request, 'first_app/home.html')
    try:
        user = User.objects.create_user(username="test", email="test@gmail.com", password="test123456")
        user.save()
    except IntegrityError as e:
        print(e)
    return HttpResponse("Welcome to home page")

def search(request):
    return render(request, 'first_app/search.html')
def about(request):
    return render(request, 'first_app/about.html')
def educative(request):
    user = User.objects.get(username = "test")
    user.email = "update@gmail.com"
    user.save()
    return HttpResponse("Welcome to the educative page!")
# def show_age(request, age):
#     return HttpResponse("I am %s years old." % age)
# def even_or_odd(request, num):
#     if(num % 2 == 0):
#         output = "%s is an even number." % num
#     else:
#         output = "%s is an odd number." % num
#     return HttpResponse(output)
def image(request):
    return render(request, 'first_app/image.html')

# def forms(request):
#     form = TestForm()
#     return render(request, 'first_app/forms.html', {'form':form})

def forms(request):
    # initial_dict={
    #     "text":"some initial data",
    #     "integer":123,
    # }
    # form = TestForm(request.POST or None, initial=initial_dict)
    form = PostModelForm(request.POST or None)
    data = "None"
    text = "None"
    if form.is_valid():
        data = form.cleaned_data
        text = form.cleaned_data.get("text")
    return render(request, 'first_app/forms.html', {'form':form, 'data':data, 'text':text})

