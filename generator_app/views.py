from django.shortcuts import render
import random
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'generator_app/home.html', {'password':'frwigbwg'})

def about(request):
    return render(request, 'generator_app/about.html')
    
def password(request):
    thepassword = ""
    characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercharacters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('1234567890')
    special = list('!£$%^&*@~#:;?.,')
    length = int(request.GET.get('length'), 12)
    inputChars = characters
    
    if request.GET.get('uppercase'):
        characters.extend(uppercharacters)
    if request.GET.get('numbers'):
        characters.extend(numbers)
    if request.GET.get('special'):
        characters.extend(special)
    
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator_app/password.html', {'password': thepassword})