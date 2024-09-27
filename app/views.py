from django.shortcuts import HttpResponse, render

# Create your views here.


def index(request):
    days_left = 60
    context = {"days_left": days_left}
    return render(request, "index.html", context=context)


def person_list(request):
    persons = [
        {"first_name": "Issa", "last_name": "Ouedraogo", "age": 25},
        {"first_name": "Yliasse", "last_name": "Tapsoba", "age": 65},
        {"first_name": "Madi", "last_name": "DAO", "age": 20},
        {"first_name": "David", "last_name": "Dah", "age": 27},
        {"first_name": "Rodrigue", "last_name": "Sawadogo", "age": 45},
    ]
    context = {"persons": persons}
    return render(request, "person.html", context=context)
