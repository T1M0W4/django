from django.shortcuts import render, get_object_or_404
from .models import Person

def person_list(request):
    people = Person.objects.all()
    return render(request, 'people/person_list.html', {'people': people})

def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'people/person_detail.html', {'person': person})


# Create your views here.