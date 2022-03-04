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
    return render(request, 'divide.html', {})