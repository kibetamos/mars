from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our services are quick'
    return render(request, 'index.html', {'feature': feature1})


def counter(request):
    # this gets the words from the name of the form in the index.html
    # if e change the name of the text are , we have o change the variable as well
    text = request.GET['text']
    number_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': number_of_words})
