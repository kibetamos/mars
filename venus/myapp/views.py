from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate #add this



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


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="templates/main/register.html", context={"register_form": form})



def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="templates/main/login.html", context={"login_form": form})

def counter(request):
    # this gets the words from the name of the form in the
    # if e change the name of the text are , we have o change the variable as well
    word = request.GET['words']
    amount_of_words = len(word.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
