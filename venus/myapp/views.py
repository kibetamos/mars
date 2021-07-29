from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # name= 'John'
    # we create  a dictionary so that we can add more files
    # lets create a dictonary called context and add aall our data therer
    # context = {
    #     'name':'PATRICK',
    #     'age':'21',
    #     'nationality':'kenyan'
    # }
    return render(request, 'index.html')


def counter(request):
    # this gets the words from the name of the form in the index.html
    # if e change the name of the text are , we have o change the variable as well
    text = request.GET['text']
    number_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': number_of_words})
