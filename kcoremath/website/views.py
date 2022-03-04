from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def add(request):
    num_1 = random.randint(a=0, b=30)
    num_2 = random.randint(a=0, b=30)

    if request.method == "POST":
        answer = request.POST.get('answer')
        old_num_1 = request.POST.get('old_num_1')
        old_num_2 = request.POST.get('old_num_2')

        correct_answer = int(old_num_1) + int(old_num_2)

        if int(answer) == correct_answer:
            my_answer = 'Correct!   ' + old_num_1 + ' + ' + old_num_2 + ' = ' + str(correct_answer) + '.'
            color = 'success'
        else:
            my_answer = 'Incorrect!   ' + old_num_1 + ' + ' + old_num_2 + ' is not ' + answer + '.  It is ' + str(correct_answer) + '.'
            color = 'danger'

        return render(request, 'add.html', context = {
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })
    
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