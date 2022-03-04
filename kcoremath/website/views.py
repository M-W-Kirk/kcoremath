from django.shortcuts import render
from random import randint
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def add(request):
    num_1 = random.randint(a=0, b=10)
    num_2 = random.randint(a=0, b=10)

    if request.method == "POST":
        answer = request.POST.get('answer')
        return render(request, 'add.html', context = {'answer':answer,})
    
    return render(request, 'add.html', context = {
        'num_1':num_1,
        'num_2':num_2,
        })

def subtract(request):
    return render(request, 'subtract.html', {})

def multiply(request):
    return render(request, 'multiply.html', {})

def divide(request):
    return render(request, 'divide.html', {})