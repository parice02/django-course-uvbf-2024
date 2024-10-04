from django.shortcuts import HttpResponse, render, redirect
from django.http import Http404

from app.forms import PersonForm
from app.models import Person

# Create your views here.

persons = [
    # {"first_name": "Issa", "last_name": "Ouedraogo", "age": 25, "pk": 1},
    # {"first_name": "Yliasse", "last_name": "Tapsoba", "age": 65, "pk": 2},
    # {"first_name": "Madi", "last_name": "DAO", "age": 20, "pk": 3},
    # {"first_name": "David", "last_name": "Dah", "age": 27, "pk": 4},
    # {"first_name": "Rodrigue", "last_name": "Sawadogo", "age": 4, "pk": 5},
    # {"first_name": "Fatasse", "last_name": "Ouedraogo", "age": 65, "pk": 6},
    # {"first_name": "Check Oumar", "last_name": "Tarnagueda", "age": 5, "pk": 7},
    # {"first_name": "Jean-Baptiste", "last_name": "Ilboudo", "age": 38, "pk": 8},
]


def index(request):
    days_left = 60
    context = {"days_left": days_left}
    return render(request, "index.html", context=context)


def person_list(request):
    context = {"persons": Person.objects.all()}
    return render(request, "person.html", context=context)


def person_profile(request, pk):
    person = Person.objects.filter(pk=pk).first()
    if not person:
        raise Http404()

    context = {"person": person}
    return render(request, "profile.html", context=context)


def person_create(request):
    form = PersonForm(data=request.POST or None)
    context = {}

    if form.is_valid():
        form.save()
        context.update({"is_valid": True})
        return redirect("app:person-list")

    context = {"form": form}
    return render(request, "form.html", context=context)
