from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


# Create your views here.
def index(request):
    features = Feature.object.all()
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.details = 'Our services are quick'
    #
    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Fast'
    # feature2.details = 'Our services are quick'
    #
    #
    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Reliable'
    # feature3.details = 'Our services are Reliable'
    #
    #
    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'Easy to use'
    # feature4.details = 'Our services are Easy to use'
    #
    #
    # feature5 = Feature()
    # feature5.id = 4
    # feature5.name = 'Affordable'
    # feature5.details = 'Our services are Affordable'
    # features = [feature1, feature2, feature3, feature4]

    # feature1 = Feature()
    # feature1.id = 5
    # feature1.name = 'Fast'
    # feature1.details = 'Our services are quick'
    return render(request, 'index.html', {'features': features})


def counter(request):
    # this gets the words from the name of the form in the index.html
    # if e change the name of the text are , we have o change the variable as well
    text = request.GET['text']
    number_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': number_of_words})
