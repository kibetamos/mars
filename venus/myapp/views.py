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
def index1(request):
    return render(request, 'index1.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


def counter(request):
    # this gets the words from the name of the form in the
    # if e change the name of the text are , we have o change the variable as well
    word = request.GET['words']
    amount_of_words = len(word.split())
    return render(request, 'counter.html',{'amount':amount_of_words})
