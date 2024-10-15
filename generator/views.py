from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    #return HttpResponse("Hello there friend")
    #return render(request, 'generator/home.html', {'password':'r@nd0mp@$$W'})
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = 10

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    length = int(request.GET.get('length',12))
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
#
# def eggs(request):
#     return HttpResponse("<h1>Eggs are tasty too</h1>")
