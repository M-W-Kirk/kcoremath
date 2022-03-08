from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import views
import random

# Create your views here.
'''
def login(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('pass_word')
        if (str(username) == 'Caramia' and str(password) == '246810'):
            return render(request, 'home.html', {})
        else:
            outcome = 'OH NO!!!'
            my_answer = 'It looks like your username or password is incorrect. Please try again.'
            color = 'danger'
            return render(request, 'login.html', {
                'outcome':outcome,
                'my_answer':my_answer,
                'color':color,
            })
    return render(request, 'login.html', {})
'''
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html', {
                'user':user,
            })
        if user is None:
            outcome = 'OH NO!!!'
            directions = 'It looks like your username or password is incorrect. Please try again.'
            color = 'danger'
            return render(request, 'login2.html', {
                'outcome':outcome,
                'directions':directions,
                'color':color,
            })
    else:
        return render(request, 'login2.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You've been logged out. See you soon."))
    return redirect('logout')

def home(request):
    return render(request, 'home.html', {})

def add(request):
    num_1 = random.randint(a=0, b=30)
    num_2 = random.randint(a=0, b=30)

    if request.method == "POST":
        answer = request.POST.get('answer')
        old_num_1 = request.POST.get('old_num_1')
        old_num_2 = request.POST.get('old_num_2')

        if not answer:
            outcome = 'Hey!!!   '
            my_answer = 'It looks like you forgot to submit your solution in the Answer Box below.'
            color = 'warning'
            return render(request, 'add.html', {
                'outcome':outcome,
                'my_answer':my_answer,
                'num_1':num_1,
                'num_2':num_2,
                'color':color
            })

        correct_answer = int(old_num_1) + int(old_num_2)

        if int(answer) == correct_answer:
            outcome = 'Correct!   '
            my_answer = old_num_1 + ' + ' + old_num_2 + ' = ' + str(correct_answer) + '.'
            color = 'success' 
        else:
            outcome = 'Incorrect!   '
            my_answer = old_num_1 + ' + ' + old_num_2 + ' is not ' + answer + '.  It is ' + str(correct_answer) + '.'
            color = 'danger'

        return render(request, 'add.html', context = {
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            'outcome':outcome,
            })
    
    return render(request, 'add.html', context = {
        'num_1':num_1,
        'num_2':num_2,
        })

def subtract(request):
    num_1 = random.randint(a=0, b=30)
    num_2 = random.randint(a=0, b=30)

    if request.method == "POST":
        answer = request.POST.get('answer')
        old_num_1 = request.POST.get('old_num_1')
        old_num_2 = request.POST.get('old_num_2')

        if not answer:
            outcome = 'Hey!!!   '
            my_answer = 'It looks like you forgot to submit your solution in the Answer Box below.'
            color = 'warning'
            return render(request, 'subtract.html', {
                'outcome':outcome,
                'my_answer':my_answer,
                'num_1':num_1,
                'num_2':num_2,
                'color':color
            })

        correct_answer = int(old_num_1) - int(old_num_2)

        if int(answer) == correct_answer:
            outcome = 'Correct!   '
            my_answer = old_num_1 + ' - ' + old_num_2 + ' = ' + str(correct_answer) + '.'
            color = 'success'
        else:
            outcome = 'Incorrect!   '
            my_answer = old_num_1 + ' - ' + old_num_2 + ' is not ' + answer + '.  It is ' + str(correct_answer) + '.'
            color = 'danger'

        return render(request, 'subtract.html', context = {
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            'outcome':outcome,
            })
    
    return render(request, 'subtract.html', context = {
        'num_1':num_1,
        'num_2':num_2,
        })

def multiply(request):
    num_1 = random.randint(a=0, b=10)
    num_2 = random.randint(a=0, b=10)

    if request.method == "POST":
        answer = request.POST.get('answer')
        old_num_1 = request.POST.get('old_num_1')
        old_num_2 = request.POST.get('old_num_2')

        if not answer:
            outcome = 'Hey!!!   '
            my_answer = 'It looks like you forgot to submit your solution in the Answer Box below.'
            color = 'warning'
            return render(request, 'multiply.html', {
                'outcome':outcome,
                'my_answer':my_answer,
                'num_1':num_1,
                'num_2':num_2,
                'color':color
            })

        correct_answer = int(old_num_1) * int(old_num_2)

        if int(answer) == correct_answer:
            outcome = 'Correct!   '
            my_answer = old_num_1 + ' x ' + old_num_2 + ' = ' + str(correct_answer) + '.'
            color = 'success'
        else:
            outcome = 'Incorrect!   '
            my_answer = old_num_1 + ' x ' + old_num_2 + ' is not ' + answer + '.  It is ' + str(correct_answer) + '.'
            color = 'danger'

        return render(request, 'multiply.html', context = {
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            'outcome':outcome,
            })
    
    return render(request, 'multiply.html', context = {
        'num_1':num_1,
        'num_2':num_2,
        })

def divide(request):
    num_1 = random.randint(a=0, b=10)
    num_2 = random.randint(a=1, b=10)

    if request.method == "POST":
        answer = request.POST.get('answer')
        old_num_1 = request.POST.get('old_num_1')
        old_num_2 = request.POST.get('old_num_2')

        if not answer:
            outcome = 'Hey!!!   '
            my_answer = 'It looks like you forgot to submit your solution in the Answer Box below.'
            color = 'warning'
            return render(request, 'divide.html', {
                'outcome':outcome,
                'my_answer':my_answer,
                'num_1':num_1,
                'num_2':num_2,
                'color':color
            })

        correct_answer_1 = int(old_num_1) / int(old_num_2)
        correct_answer_2 = round(correct_answer_1, 2)

        if float(answer) == correct_answer_2:
            outcome = 'Correct!   '
            my_answer = old_num_1 + ' / ' + old_num_2 + ' = ' + str(correct_answer_2) + '.'
            color = 'success'
        else:
            outcome = 'Incorrect!   '
            my_answer = old_num_1 + ' / ' + old_num_2 + ' is not ' + answer + '.  It is ' + str(correct_answer_2) + '.'
            color = 'danger'

        return render(request, 'divide.html', context = {
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            'outcome':outcome,
            })
    
    return render(request, 'divide.html', context = {
        'num_1':num_1,
        'num_2':num_2,
        })
    